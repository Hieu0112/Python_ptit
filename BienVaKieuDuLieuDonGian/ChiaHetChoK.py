# a = list(map(int, input().split()))
# so = []
# for i in range(a[0]//a[1],a[2]//a[1]+1):    
#     res = a[1] * i - a[0]
#     if res > 0:
#         so.append(str(res))
# print(-1 if len(so)==0 else " ".join(so))
a,K,N=[int(x) for x in input().split()]
so=[]
for i in range(K-(a%K),N-a+1,K):
    if((i+a)%K==0):
        so.append(str(i))
print(-1 if len(so)==0 else " ".join(so))