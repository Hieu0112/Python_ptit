import datetime
n,m=map(int,input().split())
KIND=[]
for i in range(n):
    KIND.append(input())
def Ngay(s):
    x=s.split('/')
    return datetime.datetime(int(x[2]),int(x[1]),int(x[0]))
class Phim:
    def __init__(self,ma,kind,date,stt,number):
        self.ma = "P{}{}{}".format(ma//100,(ma%100)//10,(ma%100)%10)
        self.kind = KIND[int(kind[2:])-1]
        self.date = date
        self.stt = stt
        self.number = number
    def __str__(self):
        return self.ma +" "+self.kind+" "+self.date+" "+self.stt+" "+self.number
lst=[Phim(i+1,input(),input(),input(),input()) for i in range(m)]
lst.sort(key=lambda x: (Ngay(x.date),x.number,-1*int(x.number)))
for i in lst:
    print(i)