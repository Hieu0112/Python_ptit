def Doiso(Str,a,b):
    return int(Str.replace(chr(a+ord('0')),chr(b+ord('0'))))
for _ in range(int(input())):
    a , b = map(int ,input().split())
    s=input()
    a1=s.split()
    if len(a1)==2:
        x=a1[1]
        y=a1[0]
    else :
        y=s
        x=input()
    smin=min(a,b)
    smax=max(a,b)
    res_min=Doiso(x,smax,smin) + Doiso(y,smax,smin)
    res_max=Doiso(x,smin,smax) + Doiso(y,smin,smax)
    print(res_min,end=' ')
    print(res_max)
