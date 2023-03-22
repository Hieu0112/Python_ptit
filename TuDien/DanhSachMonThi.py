t=int(input())
a=[]
b=[]
vt=0
while t>0:
	t-=1
	s=input()
	b.append(s+str(vt))
	s+=" "+input()
	s+=" "+input()
	a.append(s)
	vt+=1
b=sorted(b)
for i in range(len(b)):
	print(a[int(b[i][len(b[i])-1])])