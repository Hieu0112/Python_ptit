t=int(input())
s=input()
a=[]*t
dem=0
for i in s.split():
	a.append(int(i))
for i in range(t-1):
	if a[i]!=a[i+1]:
		dem+=1
print(dem)		