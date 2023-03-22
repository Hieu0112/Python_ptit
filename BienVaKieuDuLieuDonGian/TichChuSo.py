for _ in range(int(input())):
    s=1
    for i in input():
        if int(i)!=0:
            s*=int(i)
    print(s)