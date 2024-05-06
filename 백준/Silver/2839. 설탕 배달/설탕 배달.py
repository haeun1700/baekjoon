n = int(input())

dp = [999_999] * max(n+1, 6)
dp[3] = dp[5] = 1 

for i in range(6, n+1):
    dp[i] = min(dp[i-3]+1, dp[i-5]+1) 

print(-1 if dp[n] >= 999_999 else dp[n])