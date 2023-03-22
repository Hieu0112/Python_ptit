n=int(input())
lst=[int(a) for a in input().split()]
ok=True
while ok:
    ok=False
    x=0
    for i in range(len(lst)-1):
        if i+1<=len(lst)-1-x:
            if (lst[i]+lst[i+1])%2==0:
                lst.pop(i)
                lst.pop(i)
                x+=2
                ok=True
    if(ok==False): break
print(len(lst))