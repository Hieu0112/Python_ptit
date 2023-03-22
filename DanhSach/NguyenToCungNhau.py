def GCD(a,b):
	if b==0:return a
	return GCD(b,a%b)
T = int(input())
a=[int(j) for j in input().split()]
a=sorted(a)
kt=0
for j in range(len(a)):
	for z in range(j+1,len(a)):
		if GCD(a[j],a[z])==1:
			print(a[j],end=' ')
			print(a[z])