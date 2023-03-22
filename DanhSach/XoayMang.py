for _ in range(int (input())):
    n,d=map(int,input().split())
    a=[x for x in input().split()]
    a=a[d:]+a[:d]
    print(" ".join(a))