class sotay():
    def __init__(self,ngay,ten,sdt):
        self.ngay = ngay
        self.ten = ten
        self.sdt =sdt
        self.ktra =self.ten.split()[-1]
lst = []
with open("SOTAY.txt") as f:
    a = f.readline().strip()
    while a!="":
        if a.split()[0]=="Ngay":
            ngay = a.split()[1]
            ten = f.readline().strip()
            sdt = f.readline().strip()
        else:      
            ten = a
            sdt = f.readline().strip()
        x = sotay(ngay,ten,sdt)
        lst.append(x)
        a = f.readline().strip()  
lst = sorted(lst, key = lambda x: (x.ktra,x.ten))
for i in lst:
    print(i.ten+":",i.sdt,i.ngay)