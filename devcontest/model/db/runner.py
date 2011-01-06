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

		if os.path.isfile(out):
			if os.path.getmtime(file) < os.path.getmtime(out):
				return out
			else:
				os.remove(out)

		name = os.path.basename(file).split(".")[0]
		params = self.pushFileName(self.compile, {"%f":file, "%o":out, "%c":name})

		p = subprocess.Popen(params, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		p.wait()

		try:
			self.compileErrors = p.stderr.read()
		except:
			self.compileErrors = ''

		if not os.path.isfile(out) and not self.compileErrors:
			self.compileErrors = p.stdout.read()

		return out

	def pushFileName(self, command, dict):
		command = command.replace(" ", "|")

		for k in dict:
			command = command.replace(k, dict[k])

		list = command.split("|")
		return list

	def ListToText(self, l):
	    s = ''
	    for i in l:
		s += i+" "
	    return s.strip()
	
	def toUnicode(self, str):
	    try:
		str = unicode(str, errors='ignore')
	    except:
		pass
	    return str

	def exe(self, file, fileIn=None, time_limit=10, memory_limit=10*1024, i=None):
		err = ""
		ret = ""
		status = False
		self.compileErrors = ""

		if self.compile:
			try:
				fileToCompile = str(file)
				file = ""
				file = self.exeCompile(fileToCompile)
			except:
				self.compileErrors = _("Error in compilation")

		if (not self.compileErrors) or os.path.isfile(file):
			params = self.pushFileName(self.run, {"%f":'"'+file+'"'})
			
			#if (i is not None):
			#	params += [str(i)]

			strParams = self.ListToText(params)
			strUlimit = ""
			if time_limit>0 and memory_limit>0:
				strUlimit = 'ulimit -t ' + str(time_limit) + " -v " + str(memory_limit) + "; "
		
			sh = open(file+".sh", "w")
			sh.write(self.sudo + "-H bash -c '"+strUlimit+strParams+"';\n")
			sh.close()

			p = subprocess.Popen(['sh', file+'.sh'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

			if fileIn:
				f = open(fileIn, 'r')
				try:
					p.stdin.write(f.read())
					p.stdin.close()
				except:
					pass
				f.close()

			while True:
				if p.poll() is not None:
					status = True
					break

			if not err:
				ret = p.stdout.read()
				err = p.stderr.read()

		if not err and ('error' in ret):
			err = ret

		return {
			"status": status,
			"return": self.toUnicode(ret),
			"errors": self.toUnicode(err),
			"compile": self.toUnicode(self.compileErrors)
		}


	__str__ = __unicode__

orm.mapper(Runner, runners_table)
