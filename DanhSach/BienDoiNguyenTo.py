a = [0] * 10001
b=[]
for i in range(2,10001) :
    if a[i] == 0 :
        for j in range(i*i, 10001,i) :
            a[j]= 1
        b.append(i)
n=int(input())
kq=0
arr=[int(i) for i in input().split()]
for i in arr:
	Min=10**5
	for j in b:
		Min=min(Min,abs(i-j))
		if j>i :
			break
	kq=max(kq,Min)
print(kq)