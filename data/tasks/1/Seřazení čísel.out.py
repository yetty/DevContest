line = raw_input()

l = line.split()
n = []
for i in l:
    n.append(int(i))
n.sort()

out = ""
for i in n:
    out = out+" "+str(i)

print out.strip()