for _ in range(int(input())):
    n=input()
    res="YES"
    for i in range(len(n)-2):
        if n[i]!=n[i+2]:
            res="NO"
            break
    print(res)