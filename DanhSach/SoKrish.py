def gt(n):
    if n==0: return 1
    return n*gt(n-1)
for _ in range(int(input())):
    a = input()
    b,sum = list(a),0
    for c in b:
        sum += gt(int(c))
    print("Yes" if str(sum)==a else "No")