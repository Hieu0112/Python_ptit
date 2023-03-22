n,m=[int(i) for i in input().split()]
a=[]
Max=0
for i in range(n):
	a.append([int(i) for i in input().split()])
for i in range(n):
	for j in range(m):
		if len(str(a[i][j]))>1 \
		and str(a[i][j])==str(a[i][j])[::-1]\
		 and a[i][j]>Max :
			Max=a[i][j]
if Max>0:
	print(Max)
	for i in range(n):
		for j in range(m):
			if a[i][j]==Max:
				print(f'Vi tri [{i}][{j}]')
else:
	print('NOT FOUND')