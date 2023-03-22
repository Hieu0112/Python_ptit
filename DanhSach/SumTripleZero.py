for _ in range(int(input())):
	n=int(input())
	a=[]
	s=input()
	dem=0
	for i in s.split():
		a.append(int(i))
	a=sorted(a)
	dem = 0
	for i in range(0,len(a)-2):
		l=i+1
		r=len(a)-1
		x = a[i]
		while l<r:
			if x+a[l]+a[r]==0:
				dem+=1
				l+=1
			elif x+a[l]+a[r]<0:
				l+=1
			else: 
				r-=1
	print(dem)