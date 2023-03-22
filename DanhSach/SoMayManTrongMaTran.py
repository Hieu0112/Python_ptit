import math
def nt(i):
	if i<2:
		return False
	for j in range(2,int(math.sqrt(i))+1):
		if i%j==0:
			return False
	return True
n,m=[int(i) for i in input().split()]
a=[]
Max=0
Mix=0
Min=99999999999
for i in range(n):
	a.append([int(i) for i in input().split()])
	Mix=(max(max(a[i]),Mix))
	Min=(min(min(a[i]),Min))
for i in range(n):
	for j in range(m):
		if a[i][j]==Mix-Min and a[i][j]>Max :
			Max=a[i][j]
if Max>0:
	print(Max)
	for i in range(n):
		for j in range(m):
			if a[i][j]==Max:
				print('Vi tri [%d][%d]'%(i,j))
else:
	print('NOT FOUND')