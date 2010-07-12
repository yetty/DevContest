numbers = raw_input()
l = numbers.split()

max = -1

for i in l:
    if int(i) > max:
        max = int(i)

print max