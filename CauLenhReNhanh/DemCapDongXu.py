import math

t = int(input())
row,cow =[0]*t,[0]*t
for i in range(t):
    s = list(input())
    for j in range(t):
        if s[j]=='C':
            row[i] +=1
            cow[j] +=1
kq =0
for c in row+cow:
    kq += math.comb(c,2)
print(kq)
