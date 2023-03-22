P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    s=input()
    if s=="0":
        break
    a=s.split()
    K=int(a[0])
    res=""
    for i in a[1]:
        res=P[(P.index(i)+K)%28]+res
    print(res)
