for _ in range(int(input())):
    n=input()
    dem=0
    ok=False
    while True:
        if int(n)%7==0 or dem>1000:
            ok=True
            break
        dem+=1
        n=str(int(n)+int(n[::-1]))
    print(n if ok else -1)