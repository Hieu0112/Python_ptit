for _ in range(int(input())):
    n=input()
    print("YES" if(n[:2]==n[len(n)-2:]) else "NO")
    print(n[len(n)-2:])