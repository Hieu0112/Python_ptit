for _ in range(int(input())):
    n=sum(map(lambda x:int(x), input()))
    print("YES" if n%3==0 else "NO")