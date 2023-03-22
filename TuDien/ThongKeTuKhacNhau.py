import re
Set={}
def cmp(item):
	x=item.split()
	n=x[0]
	m=int(x[1])
	return (500-m,n)
n=int(input())
s=[]
while n>0:
	n-=1
	s+= re.split("[^a-zA-Z0-9]",input())
for i in s:
	i=i.lower()
	if i in Set:
		Set[i]+=1
	else:
		Set[i]=1
a=[]
# print(s)
for i in Set:
	if(len(i)>0):
		a.append(str(i)+" "+str(Set[i]))
a=sorted(a,key=cmp)
for i in a:
	print(i)