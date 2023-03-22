t=int(input())
while t>0:
	t-=1
	dem=0
	n,p=[int(i) for i in input().split()]
	for i in range(2,n+1):
		x=i	
		while x%p==0:
			dem+=1
			x//=p
	print(dem)