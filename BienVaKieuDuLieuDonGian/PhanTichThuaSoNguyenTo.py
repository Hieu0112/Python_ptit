for _ in range(int(input())):
    n=int(input())
    print("1 ",end="")
    dem=0
    while n%2==0:
        dem+=1
        n/=2
    if dem!=0:
        print("* 2^{}".format(dem),end=" ")
    for i in range(3,int(n**0.5)+1,2):
        dem=0
        while n%i==0:
            dem+=1
            n//=i
        if dem!=0:
            print("* {}^{}".format(i,dem),end=" ")
    if(n!=1):
        print("* {}^1".format(int(n)),end="")
    print()   

