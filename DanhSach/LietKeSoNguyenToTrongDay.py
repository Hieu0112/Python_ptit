def nt(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
res={}
a=[int(x) for x in input().split()]
for i in a:
    if nt(i):
        if i in res:
            res[i]+=1
        else:
            res[i]=1
for i in res:
    print(i,res[i],sep=" ")