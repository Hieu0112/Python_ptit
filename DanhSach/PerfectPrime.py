def nt(n):
    if n<2: return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0: 
            return False
    return True
for _ in range(int(input())):
    n,sum,kq = input(),0,0
    if nt(int(n))==1 and nt(int(n[::-1]))==1:
        for a in n:
            if nt(int(a))==False:
                print("No")
                kq = 1
                break
            else: 
                sum += int(a)
        if kq==0:
            if nt(sum) == 1:
                print("Yes")
            else:
                print("No")
    else : 
        print("No")