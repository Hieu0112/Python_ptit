def kiemtra(s):
    if len(s) < 2: return -1
    c=-1
    x= s[::-1]
    for i in range(0,len(s)-1):
        if x[i]<x[i+1]:
            c = i+1
            break
    if c==-1: return -1
    maxc,vitri =" ", -1
    for i in range(c):
        if maxc<=x[i]<x[c]:
            maxc = x[i]
            vitri = i
    # doi cho s vi tri va s c
    x = x[:vitri]+x[c]+x[vitri+1:c]+x[vitri]+x[c+1:]
    if x[len(s)-1]=="0": return -1
    return x[::-1]
t = int(input())
while t>0:
    s = input()
    print(kiemtra(s))
    t -=1
#213454 10055005