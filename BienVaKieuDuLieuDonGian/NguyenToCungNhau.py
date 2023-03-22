import math
N,K=[int(x) for x in input().split()]
dem=0
for i in range(10**(K-1),10**K):
    if(math.gcd(i,N)==1):
        print(i,end=" ")
        dem+=1
        if(dem%10==0):
            print()