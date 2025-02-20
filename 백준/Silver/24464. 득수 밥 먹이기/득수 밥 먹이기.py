MOD = 1000000007

n = int(input())
dp = [[0,0,0,0,0] for i in range(n+1)]

dp[1] = [1,1,1,1,1]
for i in range(2, n+1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][3] + dp[i-1][4]) % MOD
    dp[i][1] = (dp[i-1][0] + dp[i-1][3] + dp[i-1][4]) % MOD
    dp[i][2] = (dp[i-1][0] + dp[i-1][4]) % MOD
    dp[i][3] = (dp[i-1][0] + dp[i-1][1]) % MOD
    dp[i][4] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % MOD

print(sum(dp[n]) % MOD)