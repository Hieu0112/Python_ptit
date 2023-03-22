for e in range(int(input())):
    s = input().split()
    a,b,c,dem=1,0,0,0
    while dem<int(s[1]):
        dem +=1
        c = a+b
        a,b=b,c
        if dem>=int(s[0]): print(c,end=" ")
    print()