T = int(input())
for t in range(T):
    n = int(input())
    dp = [0] * 12
    dp[1], dp[2], dp[3] = 1, 2, 4
    for i in range(4, 11):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
        if i == n:
            print(dp[n])
            break
    else:
        print(dp[n])