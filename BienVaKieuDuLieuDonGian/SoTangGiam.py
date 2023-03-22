def checktang(n):
    for i in range(len(n)-1):
        if(n[i]>=n[i+1]):
            return False
    return True
for _ in range(int(input())):
    n= input()
    x=0
    for i in range(len(n)-1):
       if n[i]>=n[i+1]:
        x=i
        break
    if len(n)>=3 and checktang(n[:x+1]) and checktang(n[x:][::-1]):
        print("YES")
    else:
        print("NO")