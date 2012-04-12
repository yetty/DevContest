#!/usr/bin/env python

from settings.base import *

try:
	from settings.local import *
except ImportError:
	pass
