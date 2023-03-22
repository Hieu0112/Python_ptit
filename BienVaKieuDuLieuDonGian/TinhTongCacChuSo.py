for _ in range(int(input())):
    s = input()
    lst,sum=[],0
    for c in s:
        if c.isnumeric(): sum+=int(c)
        else: lst +=[c]
    lst.sort()
    print("".join(lst)+str(sum))