#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os, datetime
import sqlalchemy as sa
from sqlalchemy import orm

import codecs

from devcontest.model import meta
from devcontest.model.meta import Session

from pylons import config

sources_table = sa.Table('sources', meta.metadata,
	sa.Column('id', sa.types.Integer(), primary_key=True),
	sa.Column('contest_id', sa.types.Integer(), sa.ForeignKey('contests.id')),
	sa.Column('task_id', sa.types.Integer(), sa.ForeignKey('tasks.id')),
	sa.Column('user_id', sa.types.Integer(), sa.ForeignKey('users.id')),
	sa.Column('file', sa.types.String()),
	sa.Column('errors', sa.types.String()),
	sa.Column('status', sa.types.Boolean()),
	sa.Column('datetime', sa.types.DateTime()),
	sa.Column('points', sa.types.Integer()),
)

class Source(object):
	path = ''
	source = ''
	status = False

	def __init__(self, contest_id, task_id, user_id, file, errors=None, points=0):
		self.contest_id = contest_id
		self.task_id = task_id
		self.user_id = user_id
		self.file = file
		self.errors = errors
		self.points = points

		self.status = False
		self.datetime = datetime.datetime.now()
		self.source = self._load()

	def getType(self):
		parts = self.file.split(".")
		return parts[-1]

	def _save(self, content):
		f = codecs.open(self.getPath(), 'w', 'utf-8')
		try:
			f.write(content)
			pass
		except:
			f.close()

	def getFile(self):
		return open(self.getPath(), 'r')

	def getPath(self):
		if self.path=='':
			self.path = config.get('sources_dir')

		if not os.path.isdir(os.path.join(self.path, str(self.user_id))):
			os.mkdir(os.path.join(self.path, str(self.user_id)))
		if not os.path.isdir(os.path.join(self.path, str(self.user_id), str(self.task_id))):
			os.mkdir(os.path.join(self.path, str(self.user_id), str(self.task_id)))

		return os.path.join(self.path, str(self.user_id), str(self.task_id), self.file)

	def _load(self):
		try:
			f = codecs.open(self.getPath(), 'r', 'utf-8')
			content = f.read()
			f.close()
			return content
		except:
			self._save("")

	def __unicode__(self):
		return "<Source(U:"+str(self.user_id)+";T:"+self.task_id+")"

	def commit(self):
		self._save(self.source)
		self.datetime = datetime.datetime.now()
		Session.commit()

	def load(self):
		self.source = self._load()

	__str__ = __unicode__


orm.mapper(Source, sources_table)
