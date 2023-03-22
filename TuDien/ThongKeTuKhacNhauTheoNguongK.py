import re
Set={}
def cmp(item):
	x=item.split()
	n=x[0]
	m=int(x[1])
	return (500-m,n)
n,m=[int(i) for i in input().split()]
s=""
while n>0:
	n-=1
	s+=input()+" "
s=re.sub(r'[^a-zA-Z0-9]'  ," ",s)

for i in s.split():
	i=i.lower()
	if i in Set:
		Set[i]+=1
	else:
		Set[i]=1
a=[]
for i in Set:
	a.append(str(i)+" "+str(Set[i]))
a=sorted(a,key=cmp)
for i in a:
	x,y=[str(j) for j in i.split() ]
	if int(y)>=m:
		print(i)