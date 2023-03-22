def Thap(n,a,b,c):
    if n==1:
        print(a+" -> "+c)
    else:
        Thap(n-1,a,c,b)
        Thap(1,a,b,c)
        Thap(n-1,b,a,c)
Thap(int(input()),'A','B','C')