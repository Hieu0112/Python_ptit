n=int(input())
a=[]
for i in range(n):
	a.append([int(i) for i in input().split()])
k=int(input())
s1=0
s2=0
for j in range(n):
	for i in range(n):
		if n-1-j>i:
			s1+=int(a[i][j])
		if n-1-j<i:
			s2+=int(a[i][j])
kq=abs(s1-s2)
if kq<=k:
	print("YES")
else:
	print("NO")
print(kq)