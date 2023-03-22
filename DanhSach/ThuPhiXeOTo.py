def tinhtien(s):
    s = s.split()
    loai_xe, so_ghe,huong, ngay=s[1],s[2],s[3],s[4]
    if huong == "OUT": return ngay,0
    if loai_xe =="Xe_con":
        if so_ghe =="5": return ngay,10000
        return ngay,15000
    elif loai_xe == "Xe_tai": return ngay,20000
    else:
        if so_ghe == "29": return ngay,50000
        else: return ngay,70000
t = int(input())
lst = []
for c in range(t):
    x = input()
    ngay,tien = tinhtien(x)
    xd = 0
    for c in lst:
        if c[0]==ngay:
            c[1] += tien
            xd = 1
    if xd==0: lst.append([ngay,tien])


for c in lst:
    print(c[0]+": "+str(c[1]))
