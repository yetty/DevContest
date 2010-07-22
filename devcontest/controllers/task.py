#!/usr/bin/env python
#-*- coding:utf-8 -*-
import logging, random, time, hashlib, unicodedata

import codecs

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from devcontest.lib.base import BaseController, render

log = logging.getLogger(__name__)


from devcontest.model import *
from devcontest.model.meta import Session


class TaskController(BaseController):
	task = None

	def index(self):
		self.auth(admin=True)

	def show(self, id, param=None):
		self.auth()

		self._load(id)
		c.task = self.task
		self.source = Session.query(Source).filter_by(user_id=self.user.id, task_id=id).first()
		if self.source:
			self.source.load()

		if param=="upload":
			if self._upload():
				self._runUserScript()
				self.source.commit()

		c.source = self.source
		if c.source:
			c.status = c.source.status
		else:
			c.status = False

		self.task.description = self.task.description.replace("\n", "<br>").replace("    ", "&nbsp;"*4).strip("<br>")

		return render("task.mako")

	def _upload(self):
		try:
			file = request.POST['source']
			size = len(file.value)
		except:
			return False

		fileName = file.filename.replace(" ", "_").encode('ascii', 'ignore')

		if size>1024*1024*2: # 2 MB
			return False

		if not self.source:
			self.source = Source(self.task.contest_id, self.task.id, self.user.id, fileName)
			Session.add(self.source)

		self.source.file = fileName
		self.source.source = file.value
		self.source.commit()
		return True

	def _runUserScript(self):
		r = Session.query(Runner).filter_by(lang=self.source.getType).first()
		self.source.errors = ""

		if not r:
			self.source.errors = _("Unknown file type")
			return False

		runIn = self._run(self.task.getPath("in"))
		fileIn = self._saveTmpIn(runIn['return'])

		try:
			data = r.exe(self.source.getPath(), fileIn)
		except:
			self.source.errors = _("Unexpected error")
			return False

		orig = self._run(self.task.getPath("out"), fileIn)

		if data['compile']:
			self.source.errors = data['compile']
			return False

		if data['errors']:
			self.source.errors = data['errors']
			return False

		if data['return'].strip()!=orig['return'].strip():
			self.source.errors = _("Wrong output")
			return False

		self.source.status = True


	def admin(self, id=None, param=None):
		self.auth(admin=True)
		self._load(id)

		if param=="save":
			self._save()
		if param=="remove":
			self._remove()

		c.id = self.task.id
		c.contest_id = self.task.contest_id
		c.name = self.task.name
		c.description = self.task.description
		c.example_in = self.task.example_in
		c.example_out = self.task.example_out
		c.data_in = self.task.data_in
		c.data_out = self.task.data_out

		c.run_in = self._run(self.task.getPath("in"))
		nameIn = self._saveTmpIn(c.run_in['return'])


		c.run_out = self._run(self.task.getPath("out"), nameIn)

		return render('/admin/taskEdit.mako')

	def _saveTmpIn(self, data):
		nameIn = 'data/tmp/'+hashlib.sha256(str(time.time())+str(random.randint(0,1000))).hexdigest()

		f = open(nameIn, 'w')
		f.write(data)
		f.close()

		return nameIn

	def _remove(self):
		Session.execute(tasks_table.delete().where(tasks_table.c.id==self.task.id))
		Session.execute(sources_table.delete().where(sources_table.c.task_id==self.task.id))
		Session.commit()

	def _load(self, id):
		self.task = Session.query(Task).filter_by(id=id).first()
		self.task.load()

	def _save(self):
		self.task.description = request.params['description']
		self.task.example_in = request.params['example_in']
		self.task.example_out = request.params['example_out']
		self.task.data_in = request.params['data_in']
		self.task.data_out = request.params['data_out']

		self.task.commit()

	def _run(self, file, fileIn=None):
		r = Session.query(Runner).filter_by(lang="py").first()
		get = r.exe(file, fileIn)
		return get
