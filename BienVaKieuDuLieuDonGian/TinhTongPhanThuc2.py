for _ in range(int(input())):
    n=int(input())
    s=0
    x=1
    if n%2==0:
        x+=1
    for i in range(x,n+1,2):
        s+=1/i
    print(format(round(s,6),".6f"))
    # print('%.6f'%s)