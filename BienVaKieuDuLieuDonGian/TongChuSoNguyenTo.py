import math
def check(n):
    if n<2:
        return "NO"
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return "NO"
    return "YES"
for _ in range(int(input())):
    so=sum(map(lambda x:int(x),input()))
    print(check(so))
    