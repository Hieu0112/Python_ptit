def dayso(a,n):
    if n==1: return a
    if n==2: return "1 "+str(a[0][1]-1)
    lst = []
    lst += [str((a[0][1]+a[0][2]-a[1][2])//2)]
    #a[0]+a[1]=b[0][1], a[1]+a[2]=b[1][2]
    for i in range(1,n):
        lst += [str(a[0][i] - int(lst[0]))]
    return " ".join(lst)

t = int(input())
b = []
for i in range(t):
    s = [int(x) for x in input().split()]
    b.append(s)
print(dayso(b,t))
