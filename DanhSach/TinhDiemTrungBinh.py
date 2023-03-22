n=int(input())
a=[float(i) for i in input().split()]
b=[]
Sum=0
for i in a:
	if i==max(a) or i==min(a):
		continue
	Sum+=i
	b.append(i)
print('%.2f' %(Sum/len(b)))
