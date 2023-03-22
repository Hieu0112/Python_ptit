for _ in range(int(input())):
    n=input()
    dem=n.count('0')+n.count('1')+n.count('2')
    print("YES" if dem==len(n) else "NO")