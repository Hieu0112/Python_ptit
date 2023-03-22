def crussgui(item):
	ten=""
	subgreed=0
	sub=0
	for i in item.split():
		if i.isdigit():
			if subgreed==0 :
				subgreed=int(i)
			else:
				sub=int(i)
		else:
			ten+=i+" "
	return (500-subgreed,sub,ten)
t=int(input())
a=[]
while t>0:
	t-=1
	s=input()
	n,m=[int(i) for i in input().split()]
	ss=s+" "+str(n)+" "+str(m)
	a.append(ss)
a=sorted(a,key=crussgui)
for i in a:
	print(i)
