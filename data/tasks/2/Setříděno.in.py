from random import randint

max = randint(200, 10000)
min = randint(0, max-20)

out = str(randint(min, max))

for i in range(randint(10, 60)):
    out = out+" "+str(randint(min, max))

print out