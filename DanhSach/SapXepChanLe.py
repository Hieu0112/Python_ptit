n = int(input())
a=[]
while True:
    x = input()
    a+=([int(j) for j in x.split()]) 
    if len(a)>=n:
        break
index = [int(x%2) for x in a ]
index = [int(x%2) for x in a ]
odd = []
even = []
for i in a:
    if i%2==0:
        even+=[i]
    else:
        odd+=[i]
odd.sort()
even.sort()
for i in index:
    if i==0:
        print(even[0],end=" ")
        even.pop(0)
    else:
        print(odd[len(odd)-1],end=" ")
        odd.pop()