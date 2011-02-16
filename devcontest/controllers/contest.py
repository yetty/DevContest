#!/usr/bin/env python
#-*- coding:utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from devcontest.lib.base import BaseController, render

log = logging.getLogger(__name__)


from devcontest.model import *
from devcontest.model.meta import Session


class ContestController(BaseController):
	contest = None

	def index(self):
		self.auth(admin=True)

	def rank(self, id):
		self._loadContest(id)

		if not self.contest.results and self.contest.is_running and not self.user.admin:
			return redirect_to(action="tasks")

		c.rank = self.contest.getRank(self.user.admin)
		c.contest = self.contest
		return render("rank.mako")

	def tasks(self, id):
		self.auth()

		c.list = self._loadTasks(id)
		c.timeSolved = self.timeSolved
		return render('/contestTasks.mako')

	def timeSolved(self, id):
		s = Session.query(Source).filter_by(task_id=id, user_id=self.user.id, status=True).first()

		if s:
			return s.datetime
		else:
			return "---"

	def toIndex(self, id=None):
		return redirect_to(controller="admin", action="contest", id=id, param=None)

	def admin(self, id=None, param=None):
		self.auth(admin=True)

		if not id:
			c.list = self._getContestsList()
			return render('/admin/contestList.mako')

		if param=="remove":
			self._remove(id)
			return self.toIndex()

		if param=="reset":
			self._reset(id)
			return self.toIndex()

		if id=="_" and param=="create":
			id = self._create(request.params['name'])
			return self.toIndex(id=id)

		self._loadContest(id)

		if param=="save":
			self.contest.name = request.params['contest_name']
			self.contest.mode = request.params['mode']
			
			if request.params.has_key('results'):
				self.contest.results = True
			else:
				self.contest.results = False

			Session.commit()

			return redirect_to(param=None)

		if param=="start":
			self.contest.start()
			Session.commit()
			return self.toIndex()

		if param=="stop":
			self.contest.stop()
			Session.commit()
			return self.toIndex()

		if param=="create_task":
			t = Task(self.contest.id, request.params['name'])
			Session.add(t)
			Session.commit()
			return redirect_to(controller="admin", action="task", id=t.id, param=None)

		c.list = self._loadTasks()
		c.contest = self.contest
		return render('/admin/contestTasks.mako')

	def _getContestsList(self):
		return Session.query(Contest).all()

	def _remove(self, id):
		Session.execute(contests_table.delete().where(contests_table.c.id==int(id)))
		Session.execute(tasks_table.delete().where(tasks_table.c.contest_id==int(id)))
		Session.execute(sources_table.delete().where(sources_table.c.contest_id==int(id)))
		Session.commit()

	def _reset(self, id):
		self._loadContest(id)
		self.contest.timeStart = None
		Session.commit()

	def _create(self, name):
		c = Contest(name)
		Session.add(c)
		Session.commit()
		return c.id

	def _loadContest(self, id):
		self.contest = Session.query(Contest).filter_by(id=id).first()

	def _loadTasks(self, id=None):
		if not id:
			id = self.contest.id
		return Session.query(Task).filter_by(contest_id=id).all()
