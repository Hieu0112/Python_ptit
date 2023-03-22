n,m=[int(i) for i in input().split()]
a=set(sorted(input().split()))
b=set(sorted(input().split()))
x=list(a-b)
y=list(b-a)
if(len(x)-len(y)==0):
	print("YES")
else:
	print("NO")