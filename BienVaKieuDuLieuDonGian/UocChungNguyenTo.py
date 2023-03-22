import math
def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True
for _ in range(int(input())):
    x,y=map(int,input().split())
    so=math.gcd(x,y)
    sum = 0
    for i in str(so):
        sum += int(i)
    print("YES" if is_prime(sum) else "NO")