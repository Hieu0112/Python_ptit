import math


class PhanSo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        GCD=math.gcd(self.x,self.y)
        return "{}/{}".format(self.x//GCD,self.y//GCD) 
a,b=map(int ,input().split())
PS=PhanSo(a,b)
print(PS)
