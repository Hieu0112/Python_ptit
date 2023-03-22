import re
Muc={}
Muc["A"]=100
Muc["B"]=500
Muc["C"]=200
class Dien:
    def __init__(self,ma,name,s):
        self.ma = "KH{}{}".format(ma//10,ma%10)
        self.name = re.sub("\s+"," ",name).strip().title()
        x=s.split()
        self.muc=Muc[x[0]]
        self.use=int(x[2])-int(x[1])
        self.trong,self.vuot,self.vat,self.tong=0,0,0,0
        self.Tien()
    def Tien(self):
        d=self.muc
        sd=self.use
        if sd<=d:
            self.trong=450*sd
        else:
            self.trong=450*d
            self.vuot=(sd-d)*1000
            self.vat=self.vuot//20
        self.tong=self.trong+self.vuot+self.vat
    def __str__(self) :
        return self.ma+" "+self.name+" "+str(self.trong)+" "+str(self.vuot)+" "+str(self.vat)+" "+str(self.tong)
a=[Dien(i+1,input(),input()) for i in range(int(input()))]
a.sort(key=lambda x: x.tong, reverse=True)
for i in a:
    print(i)