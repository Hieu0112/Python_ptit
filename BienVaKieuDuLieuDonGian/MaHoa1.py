for _ in range(int(input())):
    n=input()+'%'
    dem=1
    for i in range(len(n)-1):
        if(n[i]==n[i+1]):
            dem+=1
        else:
            print(dem,n[i],end="",sep="")
            dem=1
    print()