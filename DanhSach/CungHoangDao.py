thang = ['0101','0120','0219','0321','0420','0521','0621','0723','0823','0923','1023','1123','1222','1232']
cung = ['Ma Ket',"Bao Binh","Song Ngu",'Bach Duong','Kim Nguu',"Song Tu","Cu Giai",'Su Tu','Xu Nu',"Thien Binh",'Thien Yet','Nhan Ma','Ma Ket']
t = int(input())
for c in range(t):
    s = input().split()
    n = ''
    if int(s[1])<10: n ="0"+s[1]
    else: n = s[1]
    if int(s[0])<10: n+="0"+s[0]
    else: n+=s[0]
    for c in range(len(thang)):
        if n<thang[c]:
            print(cung[c-1])
            break