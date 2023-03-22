b = [True]*100000
c=[0]*1009
z=1
for i in range(2,100000):
	if b[i]:
		c[z]=i
		z+=1
		if z>1004:
			break
		for j in range(2*i,100000,i):
			b[j]=False
n,x=[int(i) for i in input().split()]
for i in range(n+1):
	print(x+c[i],end=' ')
	x=x+c[i]
