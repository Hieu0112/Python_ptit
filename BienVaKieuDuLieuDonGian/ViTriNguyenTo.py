def nt(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True
for _ in range(int(input())):
    s = input()
    kq = "YES"
    for i in range(len(s)):
        if nt(i) != nt(int(s[i])): 
            kq = "NO"
            break
    print(kq)