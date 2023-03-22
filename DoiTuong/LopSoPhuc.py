# a1 +b1i
# a2+b2i
class SoPhuc:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def APlusB(self,B):
        a1=self.a+B.a
        a2=self.b+B.b
        return SoPhuc(a1,a2)
    def AMULB(self,B):
        a1=self.a*B.a-self.b*B.b
        b1=self.a*B.b+self.b*B.a
        return SoPhuc(a1,b1)
    def __str__(self):
        dau="+"
        if self.b<0:
            dau="-"
        return str(self.a)+" "+dau+" "+str(int(abs(self.b)))+"i"
for _ in range(int(input())):
    a=[int(i) for i in input().split()]
    X=SoPhuc(a[0],a[1])
    Y=SoPhuc(a[2],a[3])
    Tong =X.APlusB(Y)
    print(Tong.AMULB(X),end=", ")
    print(Tong.AMULB(Tong))
