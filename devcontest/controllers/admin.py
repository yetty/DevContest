import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from devcontest.lib.base import BaseController, render

from devcontest.controllers.task import TaskController as Task
from devcontest.controllers.contest import ContestController as Contest
from devcontest.controllers.page import PageController as Page
from devcontest.controllers.user import UserController as User
from devcontest.controllers.runners import RunnersController as Runners

log = logging.getLogger(__name__)

class AdminController(BaseController):
	def index(self):
		return self.mrender('/admin/index.mako', admin=True)

	def users(self):
		return self.mrender('/admin/auser.mako', admin=True)

	def task(self, id=None, param=None, num=None):
		return Task().admin(id, param, num)

	def contest(self, id=None, param=None):
		return Contest().admin(id, param)

	def page(self, id=None, param=None):
		return Page().admin(id, param)

	def runners(self, id=None, param=None):
		return Runners().admin(id, param)

	def users(self, id=None, param=None):
		return User().admin(id, param)
