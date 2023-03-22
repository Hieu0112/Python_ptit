Luong=[[10,12,14,20],[10,11,13,16],[9,10,12,14],[8,9,11,13]]
Phong={}
n=int(input())
for i in range(n):
    s=input()
    vt=s.find(" ")
    Phong[s[:vt].strip()]=s[vt:].strip()
def HeSo(s):
    x=ord(s[0])-ord('A')
    Nhom=Luong[x]
    nam=int(s[1:3])
    if nam>=16:
        return Nhom[3]
    if nam>=9:
        return Nhom[2]
    if nam>=4:
        return Nhom[1]
    return Nhom[0]
class NhanVien:
    def __init__(self,ma,name,lcb,ngay):
        self.ma=ma
        self.name=name
        self.p=Phong[ma[-2:]]
        self.luong=lcb*ngay*HeSo(ma)*1000
    def __str__(self):
        return self.ma+" "+self.name+" "+self.p+" "+str(self.luong)
lst=[NhanVien(input(),input(),int(input()),int(input())) for i in range(int(input()))]
for i in lst:
    print(i)