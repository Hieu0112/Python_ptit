import itertools
n,k=[int(x) for x in input().split()]
arr=[int(x) for x in input().split()]
arr=sorted(list(set(arr)))
# a=[0]*50
# n=len(arr)
# def In():
#     for i in range(1,k+1):
#         print(a[arr[i]-1],end=" ")
#     print()
# def Try(i):
# 	for j in range(a[i-1]+1,n-k+i+1):
# 		a[i]=j
# 		if i==k:In()
# 		else:Try(i+1)
# Try(1)
res = list(itertools.combinations(arr, k))
for i in res:
	for j in i:
		print(j,end=" ")
	print()