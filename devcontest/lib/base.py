#-*- coding:utf-8 -*-
"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons import request, session

from pylons.controllers import WSGIController
from pylons.templating import render_mako as render
from pylons.controllers.util import abort, redirect_to

from pylons.i18n import get_lang, set_lang

from devcontest.model.meta import Session

class BaseController(WSGIController):
	def __before__(self, action, **params):
		self.user = None
		try:
			user = session.get('user')
			if user:
				request.environ['REMOTE_USER'] = user
				request.environ['REMOTE_USER_NAME'] = session.get('user_name')
				self.user = user
		except:
			pass

		if 'lang' in session:
			set_lang(session['lang'])


	def __call__(self, environ, start_response):
		"""Invoke the Controller"""
		# WSGIController.__call__ dispatches to the Controller method
		# the request is routed to. This routing information is
		# available in environ['pylons.routes_dict']
		try:
			return WSGIController.__call__(self, environ, start_response)
		finally:
			Session.remove()

	def auth(self, admin=False):
		try:
			if not request.environ.get('REMOTE_USER'):
				abort(401)
			if not request.environ.get('REMOTE_USER').admin and admin:
				abort(401)
		except:
			try:
				del session['user']
				request.environ['REMOTE_USER'] = None
				session.save()
			except:
				pass
			return redirect_to(controller="home", action="index", id=None, param=None)


	def mrender(self, page, admin=False):
		self.auth(admin)
		return render(page)
