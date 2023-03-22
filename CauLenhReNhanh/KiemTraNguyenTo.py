import math
def nt(n):
	if n<2 :return 0
	for i in range(2,int(math.sqrt(n))+1):
		if n%i==0:
			return 0
	return 1
Set={}
n,m = [int(i) for i in input().split()]
a=[]*n
for i in range(n):
	a.append([int(j) for j in input().split()])
for i in range(n):
	for j in range(m):
		if nt(a[i][j])==1:
			print("",end='1 ')
		else:
			print("",end='0 ')
	print("")