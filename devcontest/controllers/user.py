#!/usr/bin/env python
#-*- coding:utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from devcontest.lib.base import BaseController, render
from pylons.i18n import get_lang, set_lang, _

log = logging.getLogger(__name__)


from devcontest.model import *
from devcontest.model.meta import Session


class UserController(BaseController):
	def index(self):
		self.auth()

		c.user = self.user

		return render('user.mako')

	def save(self):
		self.auth()
		l = request.params

		if l['password'] == l['cpassword'] and l['password']!="":
			self.user.password = hash(l['password'])

		if l['mail']!="":
			self.user.mail = l['mail']

		self.user.fname = l['fname']
		self.user.lname = l['lname']
		self.user.cls = l['cls']
		Session.commit()

		return self.index()

	def top(self, count=10):
		self.auth()

		users = None
		if self.user:
			if self.user.admin:
				users = Session.query(User).all()
		if not users:
			users = Session.query(User).filter_by(admin=False).all()

		c.users = []
		for user in users:
			count = Session.query(Source).filter_by(user_id=user.id, status=True).count()
			if count:
				c.users.append({'user':user,'count':count})

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

		c.users = Session.query(User).order_by(users_table.c.cls, users_table.c.lname,  users_table.c.fname).all()
		return render('admin/user.mako')

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
