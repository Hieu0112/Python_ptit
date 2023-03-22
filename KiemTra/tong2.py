MOD = 1000000007
def C(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return (C(n-1, k) + C(n-1, k-1)) % MOD
def Bernoulli(i):
    if i == 0:
        return 1
    B = [0] * (i+1)
    C = [[0] * (i+1) for _ in range(i+1)]
    C[0][0] = 1
    for n in range(1, i+1):
        for k in range(n+1):
            C[n][k] = (C[n-1][k] + C[n-1][k-1]) % MOD
        for j in range(n):
            B[n] -= (C[n][j] * B[j]) % MOD
        B[n] //= (n+1)
        B[n] %= MOD
    return B[i]
def SumOfPowers(n, k):
    ans = 0
    for i in range(k+1):
        ans += (C(k+1, i) * Bernoulli(i) * pow(n, k+1-i, MOD)) % MOD
        ans %= MOD
    # ans += pow(k+1, MOD-2, MOD)
    # ans %= MOD
    return ans
for _ in range(int(input())):
    n,k=map(int,input().split())
    print(SumOfPowers(n,k))