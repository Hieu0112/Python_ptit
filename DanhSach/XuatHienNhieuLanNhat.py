for _ in range(int(input())):
	n = int(input())
	a = [int(x) for x in input().split()]
	count = [0]*1000009
	max = 0
	ans = a[0]
	for i in a:
		count[i]+=1
		if(count[i]>max):
			max = count[i]
			ans = i
	print(ans if max>n/2 else "NO")
