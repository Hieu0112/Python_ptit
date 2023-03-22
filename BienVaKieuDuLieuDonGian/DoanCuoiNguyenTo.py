def nt(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True
for x in range(int(input())):
    print("YES" if(nt(int(input()[-4:])))else "NO")
