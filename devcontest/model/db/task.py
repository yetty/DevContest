#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import sqlalchemy as sa
from sqlalchemy import orm

from devcontest.model import meta
from devcontest.model.meta import Session

import unicodedata

from pylons import config

tasks_table = sa.Table('tasks', meta.metadata,
	sa.Column('id', sa.types.Integer(), primary_key=True),
	sa.Column('contest_id', sa.types.Integer(), sa.ForeignKey('contests.id')),
	sa.Column('name', sa.types.Unicode()),
	sa.Column('description', sa.types.Unicode()),
	sa.Column('example_in', sa.types.Unicode()),
	sa.Column('example_out', sa.types.Unicode()),
	sa.Column('run_count', sa.types.Integer()),
	sa.Column('script_in_lang', sa.types.Unicode()),
	sa.Column('script_out_lang', sa.types.Unicode()),
)


class Task(object):
	path = ''

	def __init__(self, parent, name, description="", example_in="", example_out="", data_in="", data_out="", run_count=1, script_in_lang="py", script_out_lang="py"):
		self.contest_id = parent
		self.name = name
		self.description = description
		self.example_in = example_in
		self.example_out = example_out
		self.run_count = run_count
		self.script_in_lang = script_in_lang
		self.script_out_lang = script_out_lang

		if data_in!="":
			self._save("in."+self.script_in_lang , data_in)
			self.data_in = data_in
		else:
			self.data_in = self._load("in")

		if data_out!="":
			self._save("out."+self.script_out_lang, data_out)
			self.data_out = data_out
		else:
			self.data_out = self._load("out")

	def _save(self, postfix, content):
		f = open(self.getPath(postfix), 'w')
		if content:
			content = unicodedata.normalize('NFKD', content).encode('ascii', 'ignore')
		f.write(content)
		f.close()

	def getPath(self, postfix=""):
		if self.path=='':
			self.path = config.get('task_dir')

		if not os.path.isdir(os.path.join(self.path, str(self.contest_id))):
			os.mkdir(os.path.join(self.path, str(self.contest_id)))

		if postfix!="":
			postfix = "."+postfix

		return unicodedata.normalize('NFKD', os.path.join(self.path, str(self.contest_id), self.name+postfix)).encode('ascii','ignore')

	def _load(self, postfix):
		try:
			f = open(self.getPath(postfix), 'r')
			content = f.read()
			f.close()
			return content
		except:
			self._save(postfix, "")

	def __unicode__(self):
		return "<Task("+str(self.id)+": "+self.name+")"

	def commit(self):
		self._save("in."+self.script_in_lang, self.data_in)
		self._save("out."+self.script_out_lang, self.data_out)
		Session.commit()

	def load(self):
		self.data_in = self._load("in."+self.script_in_lang)
		self.data_out = self._load("out."+self.script_out_lang)


	__str__ = __unicode__

orm.mapper(Task, tasks_table)
