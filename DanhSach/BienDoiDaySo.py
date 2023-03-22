def DEM(a,b,c,d,e):
	dem=0
	while a!=b or a!=c or a!=d :
		a=abs(a-b)
		b=abs(b-c)
		c=abs(c-d)
		d=abs(d-e)
		e=a
		dem+=1
	print(dem)
while True:
	a,b,c,d=[int(i) for i in input().split()]
	if a==b and b==c and c==d and d==0:
		break
	else:
		DEM(a,b,c,d,a)