while True:
	n=int(input())
	if n==0:
		break
	Set={1}
	while n>1:
		Set.add(n)
		if n%2==0:
			n/=2
		else:
			n=n*3+1
	print(len(Set))