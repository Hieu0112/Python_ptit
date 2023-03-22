n=int(input())
Set={}
for i in range(n-1):
	a,b=[int(i) for i in input().split()]
	if a in Set:
		Set[a]+=1
	else:
		Set[a]=1
	if b in Set:
		Set[b]+=1
	else:
		Set[b]=1
kt="Yes"
for i in Set:
	if Set[i]!=1 and Set[i]!=n-1:
		kt="No"
		break
print(kt)