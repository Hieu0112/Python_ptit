def nt(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True
def ct(n):
    sum =0
    for i in range(len(n)):
        if (i%2 ==0 and int(n[i])%2==0) or  (i % 2 != 0 and int(n[i]) % 2 != 0): 
            sum+=int(n[i])
        else: 
            return "NO"
    if nt(sum)==1: 
        return "YES"
for _ in range(int(input())):
    print(ct(input()))