from random import randint as rand

n = rand(2, 100)
max = rand(1, 10000)
out = str(rand(1, max))

for i in range(0, n-1):
    out = out+" "+str(rand(1, max))

print out