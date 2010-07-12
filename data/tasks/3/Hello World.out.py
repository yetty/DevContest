#!/usr/bin/env python

import sys

lines = sys.stdin.read().split("\n")

print "Hello, World!"
for name in lines:
    if name:
        print "Hello, "+name+"!"
