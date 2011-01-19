#!/usr/bin/env python
#-*- coding:utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from devcontest.lib.base import BaseController, render

log = logging.getLogger(__name__)


from devcontest.model import *
from devcontest.model.meta import Session


class ArchivController(BaseController):
	def index(self):
		c.list = Session.query(Contest).filter_by(is_running=False).filter(Contest.timeStart!=None).all()
		return render('archiv.mako')

	def contest(self, id):
		c.list = Session.query(Task).filter_by(contest_id=id).all()
		c.okUsers = self._okUsers
		c.allUsers = self._allUsers
		return render('archivTasks.mako')

	def _okUsers(self, task_id):
		return Session.query(Source).filter_by(task_id=task_id, status=True).count()
	
	def _allUsers(self, task_id):
		return Session.query(Source).filter_by(task_id=task_id).count()
