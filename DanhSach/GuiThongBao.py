# for _ in range(int(input())):
# 	s=input().strip()
# 	if len(s) > 100:
# 		print(s[0:100].strip())
# 	else:
# 		print(s.strip())

n=int(input())
while n>0:
	n-=1
	s=input()
	s.strip()
	kt=0
	if (len(s)>100 and s[99]!=' ' and s[100]!=' '): kt=1
	if len(s)>100:
		s=s[0:100].strip()
	if kt==1:
		s=s[0:(s.rfind(' '))].strip()
	print(s)