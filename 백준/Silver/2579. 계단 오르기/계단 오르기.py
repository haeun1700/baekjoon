n = int(input())
st = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n + 1)]


def jump(n):
    dp[1] = st[0]
    if n >= 2:
        dp[2] = st[0] + st[1]
        for i in range(3, n + 1):
            dp[i] = st[i - 1] + max(dp[i - 2], st[i - 2] + dp[i - 3])
    return dp[n]

print(jump(n))