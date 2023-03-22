t=int(input())
while(t>0):
	t-=1
	a=[]
	b=[]
	d=[]
	n,m=[int(i) for i in input().split()]
	c=[[]*n]*n
	for i in range(n):
		a.append([int(i) for i in input().split()])
	for i in range(m):
		c=[]
		for j  in range(n):
			c.append(a[j][i])
		b.append(c)
	# print(b)
	for i in range(n):
		x=[]
		for j in range(n):
			c=0
			for k in range(m):
				c+=(a[i][k]*b[k][j])
			x.append(c)
		d.append(x)
	for i in range(n):
		for j  in range(n):
			print(d[i][j],end=' ')
		print("")