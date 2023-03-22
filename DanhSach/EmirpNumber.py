a=[0]*1000009
a[0]=1
a[1]=1
for i in range(2,1000000):
    if a[i]==0:
        for j in range(2*i,1000000,i):
            a[j]=1
for _ in range(int(input())):
    n=int(input())
    for i in range(n):
        j=int(str(i)[::-1])
        if a[i]==0 and a[j]==0 and i<j and j<n:
            print(i,j,sep=" ",end=" ")
    print()