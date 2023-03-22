import math
def isPrime(x):
    if x<2:
        return False
    else :
        for i in range(2,int(math.sqrt(x))+1):
            if x%i==0:
                return False
        return True
for _ in range(int(input())):
    n=int(input())
    dem=0
    for i in range(1,n):
        if(math.gcd(i,n)==1): dem+=1
    print("YES" if(isPrime(dem)) else "NO")