for _ in  range(int(input())):
    n=input()
    dem=0
    ok=True
    for i in range(len(n)-1):
        dem+=ord(n[i])-ord('0')
        if abs(ord(n[i])-ord(n[i+1]))!=2:
            ok=False
            break
    dem+=ord(n[-1])-ord('0')
    if abs(ord(n[-1])-ord(n[-2]))!=2 or dem%10!=0:
        ok=False
    print("YES" if ok else "NO")