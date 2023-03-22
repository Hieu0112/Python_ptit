T = int(input())
a=[int(j) for j in input().split()]
kt=0
for j in range(len(a)):
	for z in range(j+1,len(a)):
		if a[j]>a[z]:
			kt+=1
print(kt)