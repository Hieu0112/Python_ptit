import math
def kc(a,b):
    if math.ceil(a/2)<=b<=a*2: return 0
    return math.ceil(math.log(max(a,b)/min(a,b),2))-1

t = int(input())
while t>0:
    a = int(input())
    lst = [int(x) for x in input().split()]
    s = 0
    for c in range(a-1):
        s += kc(lst[c],lst[c+1])
    print(s)
    t-=1
    # 1 2 4 8 16 32 64 100