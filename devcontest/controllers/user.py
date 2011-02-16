#!/usr/bin/env python
#-*- coding:utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from devcontest.lib.base import BaseController, render
from pylons.i18n import get_lang, set_lang, _

log = logging.getLogger(__name__)

from sqlalchemy import not_
from devcontest.model import *
from devcontest.model.meta import Session


class UserController(BaseController):
	def index(self):
		self.auth()

		c.user = self.user

		return render('user.mako')

	def save(self):
		self.auth()
	
		id = self.user.id
		
		user = Session.query(User).filter_by(id=id).first()
		
		l = request.params

		if l['password'] == l['cpassword'] and l['password']!="":
			user.password = hash(l['password'])

		if l['mail']!="":
			user.mail = l['mail']

		user.fname = l['fname']
		user.lname = l['lname']
		user.cls = l['cls']

		Session.commit()
		del session['user']

		request.environ['REMOTE_USER'] = user
		request.environ['REMOTE_USER_NAME'] = session.get('user_name')
		self.user = user
		session['user'] = user
		session.save()

		return self.index() #redirect_to(controller=None)

	def top(self, id=10):
		self.auth()
	
		countShow = int(id)
		users = None
		if self.user:
			if self.user.admin:
				users = Session.query(User).all()
		if not users:
			users = Session.query(User).filter_by(admin=False).all()

		contests = Session.query(Contest).filter_by(is_running=True).all()
		runningContests = []
		for contest in contests:
			runningContests.append(contest.id)
				
		c.users = []
		for user in users:
			count = Session.query(Source).filter_by(user_id=user.id, status=True).filter(not_(Source.contest_id.in_(runningContests))).count()
			if count:
				c.users.append({'user':user,'count':count})
		c.users = sorted(c.users, key=lambda rank: (int(rank['count']), rank['user']), reverse=True)[:countShow]
		return render('top.mako')

	def admin(self, id, param):
		self.auth(admin=True)

		if id=="remove" and param:
			Session.execute(users_table.delete().where(users_table.c.id==int(param)))
			Session.commit()

		if id=="save" and param:
			params = request.params
			self._adminSave(param, params)
			return redirect_to(id="edit")

		if id=="edit" and param:
			c.user = Session.query(User).filter_by(id=int(param)).first()
			return render("admin/userEdit.mako")
		
		if id=="source_view" and param:
			c.source = Session.query(Source).filter_by(id=int(param)).first()
			c.user = Session.query(User).filter_by(id=c.source.user_id).first()
			c.task_name = self._getTaskName(c.source.task_id)
			return render("admin/viewSource.mako")

		if id=="sources" and param:
			c.user = Session.query(User).filter_by(id=int(param)).first()
			c.sources = Session.query(Source).filter_by(user_id=int(param)).all()
			c.getTaskName = self._getTaskName
			c.taskExists = self._taskExists
			return render("admin/userSources.mako")

		c.users = Session.query(User).order_by(users_table.c.lname, users_table.c.fname).all()
		return render('admin/user.mako')
	
	def _taskExists(self, id):
		task = Session.query(Task).filter_by(id=id).first()
		print task.name
		if task:
			return True
		else:
			return False

	def _getTaskName(self, id):
		task = Session.query(Task).filter_by(id=id).first()
		if task:
			return task.name

	def _adminSave(self, id, params):
		user = Session.query(User).filter_by(id=id).first()
		user.fname = params['fname']
		user.lname = params['lname']
		user.mail = params['mail']
		user.cls = params['cls']
		if params['password']!='' and params['password']==params['cpassword']:
			user.password = hash(params['password'])

		if params.has_key('admin'):
			user.admin = True
		else:
			user.admin = False
		Session.commit()
