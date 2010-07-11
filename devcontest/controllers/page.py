#!/usr/bin/env python
#-*- coding:utf-8 -*-

import logging
import os
import time

import codecs

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from devcontest.lib.base import BaseController, render


log = logging.getLogger(__name__)

class PageController(BaseController):
	path = './data/pages/'
	page = None
	extension = "html"

	def index(self, id=None):
		if not id:
			return redirect_to(controller="home", action="index", id=None)

		self.page = id

		if self._pageExists():
			self._loadPage()

			# Return a rendered template
			return render('/page.mako')
		else:
			return render('error.mako')

	def _remove(self):
		os.remove(self._filename())

	def _save(self, content):
		f = codecs.open(self._filename(), 'w', 'utf-8')
		f.write(content)
		f.close()

	def _create(self, name):
		self.page = name
		if not self._pageExists():
			f = open(self.path+self.page+"."+self.extension, "w")
			f.close()

	def _filename(self):
		return self.path+self.page+"."+self.extension

	def _pageExists(self):
		if os.path.isfile(self._filename()):
			return True
		else:
			return False

	def _loadPage(self):
		f = codecs.open(self._filename(), 'r', 'utf-8')
		content = f.read()
		f.close()

		c.name = self.page
		c.content = content

	def _getListOfPages(self):
		list = []
		for o in os.listdir(self.path):
			if os.path.isfile(self.path+o):
				name, ext = o.rsplit('.')
				if ext==self.extension:
					list.append(name)

		return list

	def admin(self, id=None, param=None):
		self.auth(admin=True)
		self.page = id
		c.lang = self.extension

		if param=="remove":
			self._remove()
			return redirect_to(id=None, param=None)

		if id=="_" and param=="create":
			self._create(request.params['url'])
			return redirect_to(id=self.page, param=None)

		if not id:
			c.list = self._getListOfPages()
			return render("admin/pageList.mako")

		if id and param=="save":
			self._save(request.params['area'])

		self._loadPage()

		return render("admin/pageEdit.mako")

