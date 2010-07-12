n = int(raw_input())

list = []
for i in range(n+2):
	tmp = []
	for j in range(n+2):
		tmp.append(0)
	list.append(tmp)

for i in range(n):
	k = i+1
	out = ""
	for j in range(k):
		if list[k-1][j-1]+list[k-1][j]<=1:
			c = 1
			out = out+" 1"
		else:
			c = list[k-1][j-1]+list[k-1][j]
			out = out+" "+str(c)
		list[k][j] = c
	print out.strip()
