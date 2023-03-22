def dk(x):
    s=0
    for i in str(x):
        s+=int(i)
    return (s,x)
for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    a=sorted(a,key=dk)
    print(*a)