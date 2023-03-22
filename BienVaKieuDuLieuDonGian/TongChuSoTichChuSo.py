for x in range(int(input())):
    s = input()
    tong,tich,kt=0,1,0
    for i in range(len(s)):
        if i%2 ==0 :
            tong+= int(s[i])
        else:
            if s[i]!="0":
                tich*=int(s[i])
                kt=tich
    print(tong,kt)

