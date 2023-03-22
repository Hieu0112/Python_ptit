n,m=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
Set={}
kq=0
Max=0
Mix=0
for i in a:
	if i not in Set:
		Set[i]=1
	else:
		Set[i]+=1
	if Set[i]>Mix:
		Mix=Set[i]
for i in Set:
	if Set[i]>Max and Set[i]!=Mix:
		kq=i
		Max=Set[i]
if kq!=0:
	print(kq)
else:
	print('NONE')

