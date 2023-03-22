a=[]
n = int(input())
res,k,dem=0,0,0
for i in range(n):
    s = input().split()
    if len(s) == 7 and k==0:
        k = 1
        res = 0
    if len(s) == 6 and k == 0:
        res = 1  
        k = 1
    if len(s)==7 and res == 0:
        res = 1
    elif len(s)==6 and res == 1:
        a.append(1)
        res = 0
    if res ==1:
        dem += 1
        if dem==4:
            a.append(2)
            dem -= 4
print(len(a))
for i in a:
    print(i)