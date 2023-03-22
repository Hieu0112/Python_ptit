import datetime

gia=[25,34,50,80]
def ChuanHoaDate(s):
    x=[int(i) for i in s.split('/')]
    return datetime.datetime(x[2],x[1],x[0])
def SoNgay(x,y):
    return int((y-x).days)+1
class HoaDon:
    def __init__(self,ma,name,sp,d1,d2,dv):
        self.ma = "KH{}{}".format(ma//10,ma%10)
        self.name = name
        self.sp = sp
        self.ngay = SoNgay(ChuanHoaDate(d1),ChuanHoaDate(d2))
        self.dv = dv
        self.g=gia[int(sp[0])-1]
    def ThanhTien(self):
        return str(self.ngay*self.g+int(self.dv))
    def __str__(self) :
        return "{} {} {} {} {}".format(self.ma,self.name,self.sp,self.ngay,self.ThanhTien())
lst=[]
for i in range(int(input())):
    lst.append(HoaDon(i+1,input().strip(),input().strip(),input().strip(),input(),input()))
lst.sort(key=lambda x:int(x.ThanhTien()),reverse=True)
for i in lst:
    print(i)