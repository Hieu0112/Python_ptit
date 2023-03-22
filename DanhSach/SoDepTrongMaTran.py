n,m=map(int ,input().split())
a=[]
Max=0
Min=9999999999
for i in range(n):
	a.append([int(i) for i in input().split()])
	Max=(max(max(a[i]),Max))
	Min=(min(min(a[i]),Min))
kc = Max - Min
res = []
for i in range(n):
	for j in range(m):
		if a[i][j] == kc:
			res.append('Vi tri [%d][%d]'%(i,j))
if len(res) == 0:
	print("NOT FOUND")
else:
	print(kc)
	for i in res:
		print(i)