import itertools
for i in list(itertools.permutations(list(input()))):
    print("".join(list(i)))