for _ in range(int(input())):
    s1=input()
    s2=s1[::-1]
    ok=True
    for i in range(len(s1)):
        if abs(ord(s1[i])-ord(s1[i-1]))!=abs(ord(s2[i])-ord(s2[i-1])):
            ok=False
            break
    print("YES" if ok else "NO")