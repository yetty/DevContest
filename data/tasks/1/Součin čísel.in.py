from random import randint as rand

n = rand(1, 200)
print n

for i in range(n):
    print str(rand(-1000, 1000))+" "+str(rand(-1000, 1000))
    
    