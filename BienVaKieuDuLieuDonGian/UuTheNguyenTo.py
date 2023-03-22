def nt(n):
    if n<2: 
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: return False
    return True
for _ in range(int(input())):
    s = input()
    TongSo=s.count('2')+s.count('3')+s.count('5')+s.count('7')
    print("YES" if nt(len(s)) and TongSo>len(s)-TongSo  else "NO")