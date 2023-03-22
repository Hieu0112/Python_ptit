def nt(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True
t = int(input())
for x in range(t):
    s = input()
    dau,cuoi = int(s[0:3]),int(s[-3:])
    if nt(dau) and nt(cuoi): print("YES")
    else: print("NO")