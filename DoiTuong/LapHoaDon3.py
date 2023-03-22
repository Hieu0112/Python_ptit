class hoadon():
    def __init__(self):
        self.ma = input()
        self.ten = input()
        self.number = int(input())
        self.don_gia = int(input())
        self.chiet_khau = int(input())
        self.tong_tien = self.number*self.don_gia-self.chiet_khau
lst = []
for c in range(int(input())):
    lst.append(hoadon())
lst.sort(key=lambda x:x.tong_tien,reverse=True)
for c in lst:
    print(c.ma,c.ten,c.number,c.don_gia,c.chiet_khau,c.tong_tien)