def nt(n):
    if n==2: return True
    for c in range(2,int(n**0.5)+1):
        if n%c==0:
            return False
    return True

t = int(input())
s = [int(x) for x in input().split()]
a = sorted(set(s),key=s.index)
tong = sum(a)
sum_left,sum_right,z=0,tong,-1
for x in a:
    z +=1
    sum_left +=x
    sum_right -=x
    if nt(sum_left) and nt(sum_right):
        print(z)
        break
if z==len(a)-1: print("NOT FOUND")
