t = int(input())
for c in range(t):
    s = input().split()
    lst = [int(x) for x in input().split()]
    maxa = lst.index(max(lst))
    lst =lst[:maxa]+[int(s[1])]+lst[maxa:]
    e = ""
    for i in lst:
        if i<0: print(i,end=" ")
        else : e +=str(i)+" "
    print(e)