#!/usr/bin/env python
#-*- coding:utf-8 -*-
import logging, random, time, hashlib, unicodedata

import codecs

import shutil
from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from devcontest.lib.base import BaseController, render
from pylons.i18n import get_lang, set_lang, _

log = logging.getLogger(__name__)


from devcontest.model import *
from devcontest.model.meta import Session

from base64 import b16encode

class TaskController(BaseController):
	task = None

	def index(self):
		self.auth(admin=True)

	def show(self, id, param=None):
		self.auth()
		self._load(id)
		
		c.task = self.task
		c.runners = Session.query(Runner).all()
		c.contest = self.contest

		self.source = Session.query(Source).filter_by(user_id=self.user.id, task_id=id).first()
		if self.source:
			self.source.load()
			c.status = self.source.status

		if param=="upload":
			if self._upload():
				c.result = self._runUserScript()
				self.source.status = c.result['status']
				self.source.points = c.result['points']
				
				err = ''
				sum = len(c.result['judges'])
				for i, result in enumerate(c.result['judges']):
					err += '<li>%s/%s: %s</li>' % (i+1, sum, result)
				
				self.source.errors = err
				self.source.commit()
		
		c.source = self.source
		if c.source:
			c.status = c.source.status
		else:
			c.status = False

		self.task.description = self.task.description.replace("\n", "<br>").replace("    ", "&nbsp;"*4).strip("<br>")

		return render("task.mako")

	def _upload(self):
		if request.POST['type']:
			response.set_cookie('source_type', request.POST['type'])

		try:
			file = request.POST['source']

			if request.POST['type'] != '*':
				file.filename += "."+request.POST['type']

			size = len(file.value)
			fileName = file.filename.replace(" ", "_").encode('ascii', 'ignore')
			fileValue = file.value
		except:
			if request.POST['code'] != '' and request.POST['type'] != '*':
				fileName = b16encode(request.POST['code'])[:16]+"."+request.POST['type']
				fileValue = request.POST['code'] 
				size = len(fileValue)
			else:
				return False


		if size>1024*10: # 10 kB 
			return False

		if not self.source:
			self.source = Source(self.task.contest_id, self.task.id, self.user.id, fileName)
			Session.add(self.source)

		self.source.file = fileName
		self.source.source = fileValue
		self.source.commit()
		return True

	def _runUserScript(self):
		result = {
			'status' : True,
			'points' : 0,
			'message' : '',
			'judges' : [],
		}
		
		r = Session.query(Runner).filter_by(lang=self.source.getType).first()

		if not r:
			result['message'] = _("Unknown file type")
			return result

		judges = Session.query(Judge).filter_by(task_id=self.task.id).all()
		for judge in judges:
			resultJudge = r.exe(self.source, judge)

			if not resultJudge['status']:
				result['status'] = False
				result['judges'].append(resultJudge['message'])
			else:
				if self.contest.mode == 2: # codex
					result['judges'].append(_('OK (%s points)') % (judge.points))
				else:
					result['judges'].append(_('OK'))
				result['points'] += judge.points
		
		if result['status']:
			result['message'] = _('The task was solved')
		else:
			result['message'] = _('The task was not solved')

		return result


	def admin(self, id=None, param=None, num=None):
		self.auth(admin=True)
	
		if param=="deljudge" and num is not None:
			Session.execute(judges_table.delete().where(judges_table.c.id==int(num)))
			Session.commit()
		
		self._load(id)		
		
		if param=="download":
			if num is None:
				download = self.task.source
				name = str(self.task.id)+"."+self.task.filetype
				size = self.task.sourceSize()
				file = download
			else:
				download = Session.query(Judge).filter_by(id=num).one()
				name = download.name
				size = download.size()
				file = download.getFile()

			response.headers['Content-Type'] = "text/plain; name=%s" % (name)
			response.headers['Content-length'] = "%s" % (size)
			response.headers['Content-Disposition'] = "attachment; filename= %s" %(name) 
			shutil.copyfileobj(file, response)
			return

		if param=="save":
			self._save()
		if param=="remove":
			contest_id = self.task.contest_id
			self._remove()
			return redirect_to(action="contest", id=contest_id, param=None)

		c.task = self.task
		if self.task.source:
			c.runner = Session.query(Runner).filter_by(lang=self.task.filetype).one()
		c.contest = self.contest
		c.runners = Session.query(Runner).all()

		return render('/admin/taskEdit.mako')

	def _saveTmpIn(self, data):
		nameIn = os.path.join(config.get('runner_tmp_dir'), hashlib.sha256(str(time.time())+str(random.randint(0,1000))).hexdigest())

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
		self.contest = Session.query(Contest).filter_by(id=self.task.contest_id).one()
		self.task.load()

	def _save(self):
		self.task.description = request.POST['description']
		self.task.example_in = request.POST['example_in']
		self.task.example_out = request.POST['example_out']
		
		self.task.filetype = request.POST['filetype']	
		if request.POST['source'] != '':
			self.task.saveSource(request.POST['source'])
	
		for i in range(int(request.POST['count'])):
			if self.contest.mode == 2: # codex
				points = request.POST['points['+str(i)+']']
			else:
				points = 0

			if request.POST.has_key('file_in['+str(i)+']') and request.POST['file_in['+str(i)+']'] != '':
				judge = Judge(self.task.id, points=points, time_limit=request.POST['time_limit['+str(i)+']'], memory_limit=request.POST['memory_limit['+str(i)+']'])
				Session.add(judge)
				Session.commit()
				judge.saveFile(request.POST['file_in['+str(i)+']'])

			elif request.POST.has_key('id['+str(i)+']'):
				judge = Session.query(Judge).filter_by(id=request.POST['id['+str(i)+']']).one()
				judge.points = points
				judge.time_limit = request.POST['time_limit['+str(i)+']']
				judge.memory_limit = request.POST['memory_limit['+str(i)+']']

		Session.commit()
		self.task.load()

	def _run(self, file, lang, fileIn=None, i=None, nolimit=False):
		r = Session.query(Runner).filter_by(lang=lang).first()

		if r:
			if nolimit:
				get = r.exe(file, fileIn, i=i, time_limit=0, memory_limit=0)
			else:
				get = r.exe(file, fileIn, i=i, time_limit=self.task.time_limit, memory_limit=self.task.memory_limit)
			return get
		else:
			return {'errors': _("This script need support of *.%s") % lang, 'return' : '', 'status':'false', 'compile' : ''}
