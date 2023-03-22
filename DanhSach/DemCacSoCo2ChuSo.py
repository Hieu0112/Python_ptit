s=input()
Set={}
a=[]
for j in range(0,len(s)-1,2):
	ss=int(s[j:j+2])
	if ss not in Set:
		Set[ss]=1
		a.append(ss)
	else:
	    Set[ss]+=1
for i in a:
	print(i,Set[i])