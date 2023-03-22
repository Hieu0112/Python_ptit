for i in range(int(input())):
    s = input().split()
    n,k=int(s[0]),int(s[1])
    z,x = 'A',66
    while n>1:
        z = z+chr(x)+z
        x +=1
        n-=1
    print(z[k-1])