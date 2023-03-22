import itertools
t = int(input())
for i in range(t):
    s = int(input())
    lst = [str(x+1) for x in range(s)]
    a = list(itertools.permutations(lst))
    print(len(a))
    for i in a[::-1]:
        print("".join(list(i)),end=" ")
    print()
