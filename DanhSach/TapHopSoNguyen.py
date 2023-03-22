n,m=[int(i) for i in input().split()]
a=set(sorted(input().split()))
b=set(sorted(input().split()))
x=list(a&b)
y=list(a-b)
z=list(b-a)
print(" ".join(sorted(list(x))))
print(" ".join(sorted(list(y))))
print(" ".join(sorted(list(z))))