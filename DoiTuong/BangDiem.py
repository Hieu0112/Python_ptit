class BangDiem:
    def __init__(self,ma,name,diem):
        self.ma = "HS{}{}".format(ma//10,ma%10)
        self.name = name
        self.diem = sum(diem)/len(diem)
    def Loai(self):
        if self.diem>=9:
            return "XUAT SAC"
        if self.diem>=8:
            return "GIOI"
        if self.diem>=7:
            return "KHA"
        if self.diem>=5:
            return "TB"
        return "YEU"
    def __str__(self):
        return  self.ma+" "+self.name+" "+str(round((self.diem*100+1)/100,1))+" "+self.Loai()
lst=[]
for i in range(int(input())):
    name =input()
    diem =[float(x) for x in input().split()]
    diem.extend(diem[:2])
    lst.append(BangDiem(i+1,name,diem))
lst.sort(key=lambda x: (x.diem),reverse=True)
for i in lst:
    print(i)
