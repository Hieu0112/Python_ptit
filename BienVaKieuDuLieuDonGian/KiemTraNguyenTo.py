def nt(n):
    if n<2: return 
    False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: 
            return False
    return True
for _ in range(int(input())):
    so = input()
    a = int(so[-4:])
    print("YES" if nt(a) else "NO")
