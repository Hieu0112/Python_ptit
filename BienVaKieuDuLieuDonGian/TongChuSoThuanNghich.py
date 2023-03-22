for _ in range(int(input())):
    l=list(input())
    so=str(sum(map(lambda x:int(x),l)))
    print("YES" if len(so)>1 and so==so[::-1] else "NO")