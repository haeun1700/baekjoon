n = int(input())
drunk = [int(input()) for _ in range(n)]

if n == 1:
    print(drunk[0])
    exit()

dp = [0] * n
dp[0] = drunk[0]
dp[1] = dp[0] + drunk[1]

if n >= 3:
    dp[2] = max(dp[1], drunk[2]+drunk[1], drunk[2]+dp[0])
    for i in range(3, n):
        dp[i] = max(dp[i-1], drunk[i] + dp[i-2], drunk[i] + drunk[i-1] + dp[i-3])

print(max(dp))