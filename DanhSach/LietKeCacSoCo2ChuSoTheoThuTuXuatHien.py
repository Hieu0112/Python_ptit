s=input()
Set=[]
i=0
while(i<len(s)-1):
	ss=s[i:i+2];
	if int(ss) not in Set:
		Set.append(int(ss))
	i+=2
for i in Set:
	print(i, end=' ')