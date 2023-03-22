import math
for _ in range(int(input())):
    n=input()
    print("YES" if math.gcd(int(n),int(n[::-1]))==1 else "NO")