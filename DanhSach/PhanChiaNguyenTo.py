import math
def nt(i):
	if i<2:
		return False
	for j in range(2,int(math.sqrt(i))+1):
		if i%j==0:
			return False
	return True
n=int(input())
a=[int(i) for i in input().split()]
b=[]
for i in a:
	if i not in b:
		b.append(i)
Sum=sum(b)
Su=0
kt=0
for i in range(len(b)):
	Su+=b[i]
	if nt(Su) and nt(Sum-Su):
		print(i)
		kt=1
		break
if kt==0:
	print('NOT FOUND')

