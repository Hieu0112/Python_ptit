n=input()
n=n[::-1]
res=""
for i in range(len(n)):
    res=res+n[i]
    if i%3==2 and i!=len(n)-1:
        res+=","
print(res[::-1])