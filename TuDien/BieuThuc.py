t=int(input())
while t>0:
	t-=1
	s=input()
	vt=1
	stack=[]
	for i in s:
		if i=='(':
			stack.append(vt)
			print(vt,end=' ')
			vt+=1
		if i==')':
			print(stack[-1],end=' ')
			stack.pop(len(stack)-1)
	print('')
