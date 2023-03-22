for _ in range(int(input())):
    so=input()
    dau=int(so[0])
    sosanh=str(dau)+"4"*(len(so)-2)+"5"
    if int(so)<int(sosanh) :
        print(str(dau)+"0"*(len(so)-1))
    else:
        print(str(dau+1)+"0"*(len(so)-1))

