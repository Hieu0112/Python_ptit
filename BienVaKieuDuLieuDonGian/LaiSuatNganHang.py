import math
for _ in range(int(input())):
    n,x,m=[float(i) for i in input().split()]
    z=math.log(m/n)/math.log(1+x/100)
    thang=int(z)
    print(thang+1 if z>thang else thang)