s=input()
k=int(input())
Set={}
a=[]
i=0
kt=0
while(i<len(s)-1):
	ss=s[i:i+2];
	if int(ss) not in Set:
		Set[int(ss)]=1
		a.append(int(ss))
	else:
	    Set[int(ss)]+=1
	i+=2
a=sorted(a)
for i in a:
	if Set[i]>=k:
		print(i,Set[i])
		kt=1
if kt==0:
	print('NOT FOUND')