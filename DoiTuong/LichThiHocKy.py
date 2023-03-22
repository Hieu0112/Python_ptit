import datetime
n,m=map(int ,input().split())
subject={}
for i in range(n):
    x=input()
    y=input()
    subject[x] = y
def Time(s):
    x=s.split()
    a=[int (i) for i in x[0].split('/')]
    b=[int (i) for i in x[1].split(':')]
    return datetime.datetime(a[2],a[1],a[0],b[0],b[1])
class Thi:
    def __init__(self,ct,mt,time,stt):
        self.ct = "T{}{}{}".format(ct//100,(ct%100)//10,(ct%100)%10)
        self.mt=mt
        self.name=subject[mt]
        self.time=time
        self.stt=stt
    def __str__(self):
        return self.ct+" "+self.mt+" "+self.name+" "+self.time+" "+self.stt
lst=[]
for i in range(m):
    s=input()
    x=s.split()
    lst.append(Thi(i+1,x[0],x[1]+" "+x[2],x[3]))
lst.sort(key=lambda x: (Time(x.time),x.ct))
for i in lst:
    print(i)