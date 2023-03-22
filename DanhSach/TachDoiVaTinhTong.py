s=input()
while True:
	if len(s)==1:
		break
	n=s[0:(len(s)//2)]
	m=s[(len(s)//2):]
	s=str(int(n)+int(m))
	print(s)