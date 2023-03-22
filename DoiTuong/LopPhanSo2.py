import math


class PhanSo:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        GCD=math.gcd(self.x,self.y)
        return "{}/{}".format(self.x//GCD,self.y//GCD)
    def Sum(self,q):
        tu=self.x*q.y+self.y*q.x
        mau=self.y*q.y
        return PhanSo(tu,mau)
a=[int(x) for x in input().split()]
PSa=PhanSo(a[0],a[1])
PSb=PhanSo(a[2],a[3])
print(PSa.Sum(PSb))