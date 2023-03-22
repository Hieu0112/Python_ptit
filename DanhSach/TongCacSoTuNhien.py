a=[0]*15
b=[]

def In(i):

	s=''
	s+='('
	for j in range(i):
		s+='%d'%(a[j])+' '
	s+='%d)'%(a[i])
	b.append(s)
def Try(Sum,vt,n,i):
	for j in range(vt,0,-1):
		# prunt(j)
		a[i]=j
		if(Sum+a[i]==n):
			In(i)
		elif Sum+a[i]<n:
			Try(Sum+a[i],j,n,i+1)
t=int(input())
while t>0:

	t-=1
	b.clear()
	n=int(input())
	Try(0,n,n,0)
	print(len(b))
	for i in b:
		print(i,end=' ')
	print('')