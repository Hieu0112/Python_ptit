import re
s=sorted(set(re.findall("[1-9][0-9]",input())))
for i in s:
	print(i,end=' ')