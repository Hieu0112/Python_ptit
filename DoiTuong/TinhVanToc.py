import functools
def VanToc(s):
    x=s.split(':')
    return 120/((int(x[0])*60+int(x[1])-6*60)/60)
class DuaXe:
    def __init__(self,name,vil,time):
        self.ma=functools.reduce(lambda x,y:x+y[0],(vil +" " +name).split(),"")
        self.name = name
        self.vil =vil
        self.v= VanToc(time)
    def __str__(self):
        return self.ma+" "+self.name+" "+self.vil+" "+str(round(self.v))+" Km/h"
a=[]
for i in range(int(input())):
    a.append(DuaXe(input(),input(),input()))
a.sort(key=lambda x:x.v,reverse=True)
for i in a:
    print(i)