def CS(n,b):
    res=""
    while(n>0):
        t=n%b
        KT=str(t)
        if t>10:
            KT=chr(55+t)
        res+=KT
        n//=b
    return res[::-1]
for _ in range(int(input())):
    a,b=map(int,input().split())
    print(CS(a,b))