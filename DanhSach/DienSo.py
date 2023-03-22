def GCD(a,b):
	if b==0:return a
	return GCD(b,a%b)
zz = int(input())
while zz>0:
	zz-=1
	dem=0
	T = int(input())
	a=[int(j) for j in input().split()]
	Min=min(a)
	Max=max(a)
	kt=0
	for j in range(Min,Max+1):
		if j not in a:
			dem+=1
	print(dem)