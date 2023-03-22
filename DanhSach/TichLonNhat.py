n=int(input())
a=[int(i) for i in input().split()]
a=sorted(a)
Max1=max(a[len(a)-1]*a[len(a)-2],a[0]*a[1])
max2=max(a[len(a)-1]*a[len(a)-2]*a[len(a)-3],a[0]*a[1]*a[len(a)-1])
print(max(Max1,max2))