#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
Dostanete dvě přirozená čísla, vrátit máte jejich nejmenší společný násobek,
tj. nejmenší přirozené číslo takové, že ho zadaná čísla beze zbytku dělí.
"""

def rozloz(n):
	prvocisla = []
	i = 2
	while i<=n:
		if(n%i==0):
			prvocisla.append(i)
			n = n/i
			i = 2
		else:
			i = i+1
	return prvocisla

def pos(n, list):
	pos = 0
	for i in list:
		if i==n:
			return pos
		pos = pos+1


a, b = raw_input().split()
pA = rozloz(int(a))
pB = rozloz(int(b))

for i in pA:
	if i in pB:
		pB[pos(i, pB)]=1

celkem = 1
for i in pA:
	celkem = celkem*i
for i in pB:
	celkem = celkem*i

print celkem
