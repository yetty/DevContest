from random import randint

max = randint(0, 1000)
min = randint(-1000, max-100) 

n = randint(3, 99)
out = str(randint(min, max))
for i in range(n-1):
    out = out+" "+str(randint(min, max))

print out