for _ in range(int(input())):
	n=int(input())
	a=sorted([int(i) for i in input().split()])
	b=sorted([int(i) for i in input().split()])
	kt=0
	for i in range(n):
		if(a[i]>b[i]):
			kt=1
			print("NO")
			break
	if kt==0:
		print("YES")