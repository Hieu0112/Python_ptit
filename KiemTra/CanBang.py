from sys import stdin
a = list(map(int, stdin.read().split()))
n, asum = 12, sum(a)
un, s = [1]*12, [0]*4
def test(ga, ind, sum, pre):
    ans = 10**8
    if ga == 3:
        s[3] = asum - s[0] - s[1] - s[2]
        MAX = max(s)
        MIN = min(s)
        return min(ans, MAX - MIN)
    for i in range(pre, n):
        if un[i]:
            un[i] = 0
            if ind == 2:
                s[ga] = sum + a[i]
                ans = min(ans, test(ga + 1, 0, 0, 0))
            else: 
                ans = min(ans, test(ga, ind + 1, sum + a[i], i + 1))
            un[i] = 1
    return ans
ACDI = test(0, 0, 0, 0)
print(ACDI)