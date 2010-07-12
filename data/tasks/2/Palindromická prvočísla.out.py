import math

def jePrvocislo(n):
	for i in range(2, int(math.sqrt(n))+1):
		if(n%i==0):
			return False
	return True

def rev(n):
	r = ''
	s = str(n)
	for c in s:
		r = c+r
	return int(r)

def main(n):
	ret = 0
	for i in range(pow(10, n-1), pow(10, n)-1):
		if jePrvocislo(i) and rev(i)==i:
			ret = i

	return ret

n = int(raw_input())
print main(n)
