n=int(input())
a=[int(i) for i in input().split()]
Min=10**9
x=0
for i in a:
	s=0
	for j in a:
		s+=abs(i-j)
	if(s<Min):
		Min=s
		x=i
print(Min,x)