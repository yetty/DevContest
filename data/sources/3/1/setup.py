#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os, sys

if(os.name=='posix'):
	" Posix - UNIX like "
	import install.posix

elif(os.name=='nt'):
	" Windows NT "
	import install.nt

elif(os.name=='mac'):
	" MacOS "
	sys.exit("We dont support Mac")

elif(os.name=='os2'):
	" OS/2 "
	sys.exit("We dont support OS/2")

elif(os.name=='ce'):
	" Windows CE "
	sys.exit("We dont support Windows CE")

elif(os.name=='java'):
	" Java "
	sys.exit("We dont support Java")

elif(os.name=='riscos'):
	" Riscos "
	sys.exit("We dont support Riscos")

else:
	sys.exit("Unknow system")
