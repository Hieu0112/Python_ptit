a=[]
x=100
y=150
z=200
def Xet(use):
        if use>100:
            return 1.05
        elif use>50:
            return 1.03
        else:
            return 1.02
class HoaDon:
    def __init__(self,ma,name,old,new):
        self.ma = "KH{}{}".format(ma//10,ma%10)
        self.name = name
        self.so=new-old
        self.phi=Xet(new-old)
    def Tien(self):
        n=self.so
        tien =0
        if n>100:
            tien+=(n-100)*z
            n=100
        if n>50:
            tien+=(n-50)*y
            n=50
        tien+=n*x
        return round(tien*self.phi)
    def __str__(self):
        return self.ma+" "+self.name+" "+str(self.Tien())
for i in range(int(input())):
    a.append(HoaDon(i+1,input(),int(input()),int(input())))
a.sort(key=lambda x:x.Tien(),reverse=True)
for i in a:
    print(i)