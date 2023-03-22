def KDq(ss):
	g,w,h,q,u=[str(i) for i in ss.split()]
	# print(w)
	s=[]
	se=[]
	if w=='?' or w=='+':
		# print("+")
		for i in range(10,100):
			for j in range(10,100):
				if i+j<100:
					a=i+j
					SS=""
					st=str(i)+" + "+str(j)+" = "+str(a)
					# se.append(st)
					for z in range(len(st)):
						if ss[z]=='?':
							SS+='?'
						else:
							SS+=st[z]
					if SS==ss:
						return st
	if w=='?' or w=='-':
		for i in range(10,100):
			for j in range(10,100):
				if i-j>9:
					a=i-j
					SS=""
					st=str(i)+" - "+str(j)+" = "+str(a)
					# se.append(st)
					for z in range(len(st)):
						if ss[z]=='?':
							SS+='?'
						else:
							SS+=st[z]
					# print(SS)
					if SS==ss:
						return st
	if w=='?' or w=='*':
		for i in range(10,100):
			for j in range(10,100):
				if i*j<100:
					a=i*j
					SS=""
					st=str(i)+" * "+str(j)+" = "+str(a)
					# se.append(st)
					for z in range(len(st)):
						if ss[z]=='?':
							SS+='?'
						else:
							SS+=st[z]
					if SS==ss:
						return st
	if w=='?' or w=='/':
		for i in range(10,100):
			for j in range(10,100):
				if i%j==0 and i/j>9:
					a=i/j
					SS=""
					st=str(i)+" / "+str(j)+" = "+str(a)
					# se.append(st)
					for z in range(len(st)):
						if ss[z]=='?':
							SS+='?'
						else:
							SS+=st[z]
					if SS==ss:
						return st
	return'WRONG PROBLEM!'
t=int(input())
while t>0:
	t-=1
	ss=input()
	print(KDq(ss))
