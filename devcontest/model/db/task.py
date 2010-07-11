#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import sqlalchemy as sa
from sqlalchemy import orm

from devcontest.model import meta
from devcontest.model.meta import Session

tasks_table = sa.Table('tasks', meta.metadata,
	sa.Column('id', sa.types.Integer(), primary_key=True),
	sa.Column('contest_id', sa.types.Integer(), sa.ForeignKey('contests.id')),
	sa.Column('name', sa.types.Unicode()),
	sa.Column('description', sa.types.Unicode()),
	sa.Column('example_in', sa.types.Unicode()),
	sa.Column('example_out', sa.types.Unicode()),
)

class Task(object):
	path = './data/tasks/'

	def __init__(self, parent, name, description="", example_in="", example_out="", data_in="", data_out=""):
		self.contest_id = parent
		self.name = name
		self.description = description
		self.example_in = example_in
		self.example_out = example_out


		if data_in!="":
			self._save("in", data_in)
			self.data_in = data_in
		else:
			self.data_in = self._load("in")

		if data_out!="":
			self._save("out", data_out)
			self.data_out = data_out
		else:
			self.data_out = self._load("out")

	def _save(self, postfix, content):
		f = open(self.getPath(postfix), 'w')
		f.write(content.encode("utf-8"))
		f.close()

	def getPath(self, postfix=""):
		if not os.path.isdir(self.path+str(self.contest_id)):
			os.mkdir(self.path+str(self.contest_id))

		if postfix!="":
			postfix = "."+postfix

		return self.path+str(self.contest_id)+"/"+self.name+postfix+".py"

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
		self._save("in", self.data_in)
		self._save("out", self.data_out)
		Session.commit()

	def load(self):
		self.data_in = self._load("in")
		self.data_out = self._load("out")


	__str__ = __unicode__

orm.mapper(Task, tasks_table)
