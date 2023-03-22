b=[]
for i in range(int(input())):
    s=input()
    if s not in b :
      b.append(s)
print(len(b))