for i in range(int(input())):
    print("Test "+str(i+1)+": "+("YES" if sorted(input())==sorted(input()) else "NO"))