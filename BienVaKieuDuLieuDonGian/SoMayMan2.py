for _ in range(int(input())):
    n=input()
    print("YES" if(n.count('4')+n.count('7')==len(n)) else "NO")