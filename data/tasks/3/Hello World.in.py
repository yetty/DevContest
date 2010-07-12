#!/usr/bin/env python

import random, hashlib

for i in range(1, 100):
    print hashlib.sha256(str(i+random.randint(0,100))).hexdigest()[0:20]
            
            