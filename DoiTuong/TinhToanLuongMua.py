class Mua:
    def __init__(self,ma,name,time,luuluong):
        self.ma = "T"+str(ma//10)+str(ma%10)
        self.name = name
        self.time=time
        self.luuluong =luuluong
    def LuongMua(self):
        return "%.2f"%(self.luuluong/self.time)
    def __str__(self):
        return self.ma+" "+self.name+" "+self.LuongMua()
def ChuanHoa(s):
        x=s.split(':')
        return int(x[0])+int(x[1])/60
a=[]
for i in range(int(input())):
    name = input()
    t1 = ChuanHoa(input())
    t2 = ChuanHoa(input())
    time=t2-t1
    luuluong =int(input())
    ok=True
    for j in a:
        if j.name == name:
            j.time+=time
            j.luuluong+=luuluong
            ok=False
    if ok:
        a.append(Mua(len(a)+1, name,time,luuluong))
for j in a:
    print(j)