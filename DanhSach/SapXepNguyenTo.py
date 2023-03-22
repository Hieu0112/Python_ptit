import math
def nt(a):
	if a<2:
	    return False
	for i in range(2,int(math.sqrt(a))+1):
	    if a%i==0: 
	        return False
	return True
n=int(input())
b=[0]*(n)
s=[]
ss=[]
a=[]
while True:
    x = input()
    a+=([int(j) for j in x.split()]) 
    if len(a)>=n:
        break
for i in range(n):
	if nt(a[i]):
		s+=[a[i]]
	else:
		b[i]=1
		ss+=[a[i]]
s=sorted(s)
j=0
jj=0
for i in range(n):
	if b[i]==0:
		print(s[0],end=' ')
		s.pop(0)
	else:
		print(ss[0],end=' ')
		ss.pop(0)