n=int(input())
while n>0:
	n-=1
	x,y,z=[int(i) for i in input().split()]
	a=[int(i) for i in input().split()]
	b=[int(i) for i in input().split()]
	c=[int(i) for i in input().split()]
	arr1=[]
	arr2=[]
	a1=0
	b1=0
	while (a1<len(a) and b1<len(b)):
		if a[a1]==b[b1]:
			arr1.append(a[a1])
			a1+=1
			b1+=1
		elif a[a1]<b[b1]:
			a1+=1
		else:
			b1+=1
	a1=0
	c1=0
	while (a1<len(arr1) and c1<len(c)):
		if arr1[a1]==c[c1]:
			arr2.append(arr1[a1])
			a1+=1
			c1+=1
		elif arr1[a1]<c[c1]:
			a1+=1
		else:
			c1+=1
	for i in arr2:
		print(i , end=' ')
	if len(arr2)==0:
		print('NO' ,end='')
	print('')
