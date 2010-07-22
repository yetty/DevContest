#!/usr/bin/env python
#-*- coding:utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from devcontest.lib.base import BaseController, render

log = logging.getLogger(__name__)


from devcontest.model import *
from devcontest.model.meta import Session


from pylons.i18n import get_lang, set_lang, _
from devcontest.lib.base import *

class AuthController(BaseController):

	def index(self):
		# Return a rendered template
		#return render('/auth.mako')
		# or, return a response
		return redirect_to(controller="home", action="index")

	def signin(self):
		try:
			login = request.params['login']
			password = request.params['password']
		except:
			return self.index()

		user = Session.query(User).filter_by(login=login, password=hash(password)).first()

		if user:
			session['user'] = user
			session.save()
			return self.index()
		else:
			c.error = _('Login failed')
			return render('/home.mako')

	def signout(self):
		try:
			del session['user']
			session.save()
		except:
			pass
		return self.index()
