def kt(a):
    a = a.split(".")
    if len(a)!=4 : return "NO"
    for c in a:
        if c.isnumeric() == False:
             return "NO"
        else:
            if int(c)<0 or int(c)>255: 
                return "NO"
    return "YES"
for _ in range(int(input())):
    print(kt(input()))