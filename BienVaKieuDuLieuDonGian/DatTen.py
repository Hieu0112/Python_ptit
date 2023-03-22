import itertools
n,k=map(int, input().split())
res=sorted(set([x for x in input().split()]))
res=list(itertools.combinations(res,k))
for i in res:
    print(" ".join(i))