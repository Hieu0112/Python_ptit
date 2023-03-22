import re
class Diem:
    def __init__(self,ma,name,diem1,diem2,diem3):
        self.ma = "SV{}{}".format(ma//10,ma%10)
        self.name = re.sub("\s+"," ",name).strip().title()
        self.diem = (diem1*3+diem2*3+diem3*2)/8
        self.xl=1
    def Tron(self):
        tmp=self.diem
        y = format(tmp,".3f")
        if y[-1]=="5": tmp = tmp+0.01
        return tmp
    def __str__(self):
        return self.ma+" "+self.name+" %.2f"%(self.Tron())+" "+str(self.xl)
n=int(input())
a=[Diem(i+1,input(),float(input()),float(input()),float(input())) for i in range(n)]
a.sort(key=lambda x: x.diem, reverse=True)
for i in range(1,n):
    if a[i].diem==a[i-1].diem:
        a[i].xl=a[i-1].xl
    else :
        a[i].xl=i+1
for i in a:
    print(i)