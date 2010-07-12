from random import randint as rand

max = rand(100, 100000)
n = rand(2, 100)

out = str(rand(1, max))

for i in range(1, n):
    out = out+" "+str(rand(1, max))

print out