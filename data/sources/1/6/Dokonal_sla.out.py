#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys

lines = sys.stdin.read().split("\n")


for i in lines:
    if i:
        if int(i) in [6, 28, 496, 8128]:
           print "Ano"
        else:
           print "Ne"
