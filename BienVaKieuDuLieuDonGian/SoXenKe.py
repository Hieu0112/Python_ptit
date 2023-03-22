def kq(n):
    if len(n)%2 ==0 or n[0]==n[1]: 
        return "NO"
    for i in range(2,len(n),2):
        if n[i]!=n[0]: return "NO"
    return "YES"
for _ in range(int(input())):
    print(kq(input()))