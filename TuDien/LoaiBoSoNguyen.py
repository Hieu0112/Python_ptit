f=open('DATA.in')
s=f.read()
a=[]
# print(s)
for i in s.split():
	if i.isdigit()==False or len(i)>9:
		a.append(i)
a.sort()
for i in a:
	print(i,end=' ')