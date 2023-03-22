a=[0]*1000009
a[0]=1
a[1]=1
for i in range(2,1000000):
    if a[i]==0:
        for j in range(2*i,1000000,i):
            a[j]=1
for _ in range(int(input())):
    dem = 0
    N=int(input())
    for i in range(N-5):
        if a[i] == 0 and a[i+6]== 0:
            if a[i+2]==0 or a[i+4]==0:
                dem+=1
    print(dem)
