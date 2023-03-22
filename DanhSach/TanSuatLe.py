t=int(input())
while t>0:
	t-=1
	n=int(input())
	Set={}
	a=[int(i) for i in input().split()]
	for i in a:
		if i not in Set:
			Set[i]=1
		else:
			Set[i]+=1
	for i in Set:
		if Set[i]%2!=0:
			print(i)