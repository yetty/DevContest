numbers = raw_input().split()

s = sorted(numbers, key = lambda i: int(i))

out = ""

for i in s:
   out = out+" "+i

print out.strip()