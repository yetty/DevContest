#-*- coding:utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect

from devcontest.lib.base import BaseController, render

log = logging.getLogger(__name__)

from devcontest.model import *
from devcontest.model.meta import Session

from pylons.i18n import get_lang, set_lang, _
from devcontest.lib.base import *


class RegistrationController(BaseController):

	def index(self):
		c.form = self.getPost()
		return render('/registration.mako')

	def check(self):
		c.success = False
		c.errors = []
		form = self.getPost()

		if not form['login']:
			c.errors.append(_("Enter your login"))
		if Session.query(User).filter_by(login=form['login']).count()!=0:
			c.errors.append(_("This login name is already used"))
		if form['password']!=form['cpassword'] or not form['password']:
			c.errors.append(_("Passwords are empty or wrong"))
		if not form['mail'] or form['mail']=="@":
			c.errors.append(_("Enter your e-mail"))
		if Session.query(User).filter_by(mail=form['mail']).count()!=0:
			c.errors.append(_("E-mail is already registered"))

		if len(c.errors)==0:
			if not self.register(form):
				c.errors.append(_("Registration failed. Sorry. Please, contact us."))
			else:
				c.success = True
				return render('/registration.mako')

		return self.index()

	def register(self, data):
		try:
			Session.add(User(data['login'], data['password'], data['mail'], data['fname'], data['lname'], data['cls']))
			Session.commit()
		except:
			return False


		return True
	def getPost(self):
		form = {"login" : "", "password": "", "cpassword" : "", "mail" : "", "fname" : "", "lname" : "", "mail" : "@", "cls" : ""}

		for k in request.params:
			if form.has_key(k):
				form[k] = request.params[k]

		return form
