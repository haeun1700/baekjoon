MOD = 1000000007
n = int(input())
dp = [[0,0,0,0,0] for i in range(n+1)]

dp[1] = [1,1,1,1,1]
for i in range(2, n+1):
    for j in range(5):
        for k in range(5):
            if j == 0 and k == 0:
                continue
            if j != 0 and k != 0 and abs(j-k) <= 1:
                continue
            dp[i][j] += dp[i-1][k]
            dp[i][j] %= MOD

print(sum(dp[n]) % MOD)