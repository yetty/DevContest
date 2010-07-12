from random import randint

n = randint(800, 1000)
print n

for i in range(n):
  print str(randint(-10000, 10000))+" "+str(randint(-10000, 10000))
