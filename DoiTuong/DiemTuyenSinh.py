import re
plusKV=[1.5,1,0]
class TuyenSinh:
    def __init__(self,ma,name,thi,dt,kv):
        self.ma = "TS{}{}".format(ma//10,ma%10)
        self.name = re.sub(r"\s+"," ",name).strip().title()
        self.diem=float(thi)+plusKV[int(kv)-1]+(1.5 if dt.lower()!="kinh" else 0)
        self.loai="Do" if self.diem>=20.5 else "Truot"
    def __str__(self):
        return self.ma+" "+self.name+" "+"%.1f"%self.diem+" "+self.loai
a=[TuyenSinh(i+1,input(),input(),input(),input()) for i in range(int(input()))]
a.sort(key=lambda x:x.diem, reverse=True)
for i in a:
    print(i)