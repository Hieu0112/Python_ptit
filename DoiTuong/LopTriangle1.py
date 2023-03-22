import sys
import math
def kc(x1,x2,x3,x4):
    return math.dist((x1,x2),(x3,x4))
line = []
for s in sys.stdin:
    for x in s.split():
        line.append(float(x))
t = int(line[0])
i = 0
for x in range(t):
    a = kc(line[i+1],line[i+2],line[i+3],line[i+4])
    b = kc(line[i+5],line[i+6],line[i+3],line[i+4])
    c = kc(line[i+1],line[i+2],line[i+5],line[i+6])
    if a<b+c and b<a+c and c<a+b:
        print(format(a+b+c,".3f"))
    else:
        print("INVALID")
    i+=6