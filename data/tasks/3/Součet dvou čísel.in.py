import random

n = random.randint(2, 1000)
print n

for i in range(1, n):
    a = random.randint(1, 100000)
    b = random.randint(1, 100000)
    print str(a)+" "+str(b)