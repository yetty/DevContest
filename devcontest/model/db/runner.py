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
	sa.Column('lang', sa.types.Unicode(), unique=True),
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

	def exe(self, source, judge, onlyResult=False):
		self.compileErrors = ''

		result = {
			'status' : True,
			'message' : '',
		}
		
		compiledFile = source.getFile().name
		
		if self.compile:
			try:
				fileToCompile = str(source.getFile().name)
				compiledFile = self.exeCompile(fileToCompile)
			except:
				self.compileErrors = 'Unexpected error during compilation' # it shoudn't show anytime.

		if self.compileErrors and not os.path.isfile(compiledFile):
			result['status'] = False
			result['message'] = _('Compilation error')
			return result
	
		if os.path.exists(compiledFile+'.output'):
				os.remove(compiledFile+'.output')

		command = "sudo -u python -H bash -c 'ulimit -t %s -v %s; %s < %s;' > %s\n" % (
					judge.time_limit,
					judge.memory_limit,
					self.ListToText(self.pushFileName(self.run, {"%f" : '"%s"' % compiledFile} )),
					judge.getFile().name,
					compiledFile+'.output',
				)

		sh = open(compiledFile+".sh", "w")
		sh.write(command)
		sh.close()
		
		process = subprocess.Popen(['sh', compiledFile+'.sh'], stderr=subprocess.PIPE)
		
		while process.poll() is None:
			pass

		error = process.stderr.read()
		if error:
			result['status'] = False
			result['message'] = error

			if 'Killed' in error:
				result['message'] = _('Time or memory limit exceeded')
			return result
		
		
		egrep = subprocess.Popen(['egrep', '-i', 'error', compiledFile+'.output'], stdout=subprocess.PIPE)
		egrepOutput = egrep.communicate()[0]

		if egrepOutput:
			result['status'] = False
			result['message'] = egrepOutput
			return result

		if onlyResult:
			return result
		
		compare = subprocess.call(['cmp', '--quiet', compiledFile+'.output', judge.getOutputFile().name])
		if compare == 1:
			result['status'] = False
			result['message'] = _('Wrong output')


		
		return result
		


	__str__ = __unicode__

orm.mapper(Runner, runners_table)
