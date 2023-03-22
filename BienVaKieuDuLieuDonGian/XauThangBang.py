for i in range(int(input())):
    a = input()
    b,t = a[::-1],0
    for y in range(1,len(a)):
        if abs(ord(a[y]) - ord(a[y-1])) != abs(ord(b[y])-ord(b[y-1])):
            print('NO')
            t = 1
            break
    if t==0:
        print('YES')

