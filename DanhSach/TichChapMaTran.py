for _ in range(int(input())):
    n,m=map(int,input().split())
    arr,brr,res=[],[],0
    for i in range(n):
        arr.append(list(map(int,input().split())))
    for i in range(3):
        brr.append(list(map(int,input().split())))
    for i in range(n-2):
        resi=[]
        for j in range(m-2):
            result=0
            for i1 in range(3):
                for j1 in range(3):
                    result +=brr[i1][j1]*arr[i1+i][j1+j]
            resi.append(result)
        res+=sum(resi)
    print(res)