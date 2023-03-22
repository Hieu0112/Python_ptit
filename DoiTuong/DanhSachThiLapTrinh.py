class team():
    def __init__(self):
        self.ma = ""
        self.name = input()
        self.truong = input()
class thisinh():
    def __init__(self):
        self.ma = "C"
        self.name = input()
        self.mateam = input()
        self.tem = ""
        self.truong = ""
tem = []
ts = []
for c in range(int(input())):
    a = team()
    a.ma = "Team0"*(2-len(str(c+1)))+str(c+1)
    tem.append(a)
for c in range(int(input())):
    a = thisinh()
    a.ma += "0"*(3-len(str(c+1)))+str(c+1)
    for i in tem:
        if i.ma == a.mateam:
            a.tem = i.name
            a.truong = i.truong
            break
    ts.append(a)
ts = sorted(ts,key = lambda x: x.name)
for c in ts:
    print(c.ma,c.name,c.tem,c.truong)