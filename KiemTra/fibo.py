n,m=map(int,input().split())
a=[int(x) for x in input().split()]
for _ in range(m):
    k=[int(x) for x in input().split()]
    if k[0]==1:
        for i in range(k[1],k[2]+1):
            a[i-1]=(a[i-1]+k[3])%(1000000007)
    else:
        res=0
        for i in range(k[1],k[2]+1):
            res+=a[i-1]
        print(res)