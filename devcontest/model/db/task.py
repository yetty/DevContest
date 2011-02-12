#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import sqlalchemy as sa
from sqlalchemy import orm

from devcontest.model import meta, Runner
from devcontest.model.meta import Session

import unicodedata, shutil

from pylons import config

tasks_table = sa.Table('tasks', meta.metadata,
	sa.Column('id', sa.types.Integer(), primary_key=True),
	sa.Column('contest_id', sa.types.Integer(), sa.ForeignKey('contests.id')),
	sa.Column('name', sa.types.Unicode()),
	sa.Column('description', sa.types.Unicode()),
	sa.Column('example_in', sa.types.Unicode()),
	sa.Column('example_out', sa.types.Unicode()),
	sa.Column('filetype', sa.types.Unicode()),
)

judges_table = sa.Table('judges', meta.metadata,
	sa.Column('id', sa.types.Integer(), primary_key=True),
	sa.Column('task_id', sa.types.Integer(), sa.ForeignKey('tasks.id')),
	sa.Column('name', sa.types.Unicode()),
	sa.Column('points', sa.types.Integer(), default=10),
	sa.Column('time_limit', sa.types.Integer(), default=1),
	sa.Column('memory_limit', sa.types.Integer(), default=1024),
)

class Judge(object):
	path = None

	def __init__(self, task_id, points=10, time_limit=1, memory_limit=1024, filetype="py"):
		self.task_id = task_id
		self.points = points
		self.name = ''
		self.time_limit = time_limit
		self.memory_limit = memory_limit

	def _getFileName(self):
		if not self.path:
			self.path = config.get('judges_dir')

		if not os.path.exists(os.path.join(self.path, str(self.task_id))):
			os.mkdir(os.path.join(self.path, str(self.task_id)))

		return os.path.join(self.path, str(self.task_id), str(self.id))
	
	def size(self):
		return os.path.getsize(self._getFileName())

	def getOutputFile(self):
		fileName = self._getFileName()+".output"
		
		if not os.path.exists(fileName):
			task = Session.query(Task).filter_by(id=self.task_id).one()
			runner = Session.query(Runner).filter_by(lang=task.filetype).one()
			runner.exe(task, self, onlyResult=True)
			shutil.move(
				os.path.join(config.get('task_dir'), str(task.contest_id), str(task.id)+"."+task.filetype+".out.output"),
				fileName
			)
		
		return open(fileName, 'r')

	def getFile(self):
		return open(self._getFileName(), 'r')

	def saveFile(self, file):
		self.name = file.filename
		Session.commit()

		f = open(self._getFileName(), 'w')
		f.write(file.value)

	def __unicode__(self):
		return "<Judge("+str(self.id)+": "+self.points+")"
	
	__str__ = __unicode__

class Task(object):
	path = ''
	filetype = ''

	def __init__(self, parent, name, description="", example_in="", example_out="", script=""):
		self.contest_id = parent
		self.name = name
		self.description = description
		self.example_in = example_in
		self.example_out = example_out
		self.filetype = ''

	def _getFileName(self):
		if self.path=='':
			self.path = config.get('task_dir')

		if not os.path.isdir(os.path.join(self.path, str(self.contest_id))):
			os.mkdir(os.path.join(self.path, str(self.contest_id)))

		self.filetype = str(self.filetype)
		return os.path.join(self.path, str(self.contest_id), str(self.id)+"."+self.filetype)

	def __unicode__(self):
		return "<Task("+str(self.id)+": "+self.name+")"

	def sourceSize(self):
		return os.path.getsize(self._getFileName())

	def getSource(self):
		return open(self._getFileName(), 'r')

	getFile = getSource

	def saveSource(self, file):
		f = open(self._getFileName(), 'w')
		f.write(file.value)

	def load(self):
		if os.path.exists(self._getFileName()):
			self.source = self.getSource()
		else:
			self.source = None

		self.judges = Session.query(Judge).filter_by(task_id=self.id).all()

	__str__ = __unicode__

orm.mapper(Judge, judges_table)
orm.mapper(Task, tasks_table)
