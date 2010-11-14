#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os, subprocess, time

import sqlalchemy as sa
from sqlalchemy import orm

from devcontest.model import meta
from pylons.i18n import get_lang, set_lang, _

import codecs

from pylons import config

runners_table = sa.Table('runners', meta.metadata,
	sa.Column('id', sa.types.Integer(), primary_key=True),
	sa.Column('lang', sa.types.Integer(), unique=True),
	sa.Column('compile', sa.types.Unicode()),
	sa.Column('run', sa.types.Unicode()),
)

class Runner(object):
	sudo = 'sudo -u python '
	compileErrors = ''

	def __init__(self, lang, compile="", run=""):
		self.lang = lang
		self.compile = compile
		self.path = config.get('runner_tmp_dir')
		self.run = run

	def __unicode__(self):
		return "<"+str(self.lang)+">"

	def exeCompile(self, file, out=None):
		if out==None:
			out = file+".out"

		name = os.path.basename(file).split(".")[0]
		params = self.pushFileName(self.compile, {"%f":file, "%o":out, "%c":name})

		p = subprocess.Popen(params, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		p.wait()

		try:
			self.compileErrors = p.stderr.read()
		except:
			self.compileErrors = ''

		return out

	def pushFileName(self, command, dict):
		command = command.replace(" ", "|")

		for k in dict:
			command = command.replace(k, dict[k])

		list = command.split("|")
		return list

	def exe(self, file, fileIn=None, limit=1):
		err = ""
		ret = ""
		status = False
		self.compileErrors = ""

		try:
			if self.compile:
				file = self.exeCompile(file)
		except:
			self.compileErrors = _("Error in compilation")

		if not self.compileErrors:
			params = self.pushFileName(self.sudo+self.run, {"%f":file})

			p = subprocess.Popen(params, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

			if fileIn:
				f = open(fileIn, 'r')
				p.stdin.write(f.read())
				p.stdin.close()
				f.close()

			timeStart = time.time()
			while True:
				if p.poll() is not None:
					status = True
					break

				if int((time.time()-timeStart)) >= limit:
					try:
						p.kill()
					except:
						pass
					status = False
					err = _("The time limit was exceeded.")
					value = None

					break

			if not err:
				ret = p.stdout.read()
				err = p.stderr.read()

		return {
			"status": status,
			"return": ret,
			"errors": err,
			"compile": unicode(self.compileErrors, errors='ignore')
		}


	__str__ = __unicode__

orm.mapper(Runner, runners_table)
