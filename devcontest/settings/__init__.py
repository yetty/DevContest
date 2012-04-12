#!/usr/bin/env python

from devcontest.settings.base import *

try:
	from devcontest.settings.local import *
except ImportError:
	pass
