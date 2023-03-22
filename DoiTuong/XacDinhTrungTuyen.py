Set={'A':"TOAN",'B':"LY",'C':"HOA"}
Uu=[2.0,1.5,1.0,0.0]
a=[]
def XL(diem):
    return "TRUNG TUYEN" if diem>=18 else "LOAI"
class XetTuyen:
    def __init__(self,ma,name,uu,x,y):
        self.ma="GV{}{}".format(ma//10,ma%10)
        self.name=name
        self.mon=Set[uu[0]]
        self.diem=float(x)*2+float(y)+Uu[int(uu[1])-1]
    def __str__(self):
        return "{} {} {} {:.1f} {}".format(self.ma,self.name,self.mon,self.diem,XL(self.diem))
for i in range(int(input())):
    a.append(XetTuyen(i+1,input(),input(),input(),input()))
a.sort(key=lambda x: x.diem, reverse=True)
for i in a:
    print(i)