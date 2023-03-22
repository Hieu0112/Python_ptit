for _ in range(int(input())):
    s=input()
    for i in s:
        if i.isalpha():
            s=s.replace(i," ")
    arr=[int(x) for x in s.split()]
    print(max(arr))