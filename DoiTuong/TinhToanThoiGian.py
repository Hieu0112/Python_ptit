def Phut(s):
    x=s.split(':')
    return int(x[0])*60+int(x[1])
class Time:
    def __init__(self,ma,name,ip,op):
        self.ma = ma
        self.name = name
        self.ip = Phut(ip)
        self.op = Phut(op)
    def Use(self):
        return self.op-self.ip
    def __str__(self):
        return "{}  {} {} gio {} phut".format(self.ma,self.name,int(self.Use()/60),int(self.Use()%60))
a=[]
for i in range(int(input())):
    a.append(Time(input(),input(),input(),input()))
a.sort(key=lambda x: x.Use(),reverse=True)
for i in a:
    print(i)