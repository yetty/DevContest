#!/usr/bin/env python
#-*- coding:utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from devcontest.lib.base import BaseController, render

log = logging.getLogger(__name__)


from devcontest.model import *
from devcontest.model.meta import Session


class RunnersController(BaseController):
	task = None

	def index(self):
		pass

	def admin(self, id=None, param=None):
		self.auth(admin=True)

		if param=="remove":
			Session.execute(runners_table.delete().where(runners_table.c.id==int(id)))
			Session.commit()

		if id=="save":
			self._save()

		c.list = Session.query(Runner).all()

		return render('/admin/runners.mako')

	def _save(self):
		r = Runner(request.params['lang'], request.params['compile'], request.params['run'])
		Session.add(r)
		Session.commit()
