T = int(input())
a=[int(j) for j in input().split()]
Min=min(a)
Max=max(a)
for j in range(1,Max+2):
	if j not in a:
		print(j)
		break
