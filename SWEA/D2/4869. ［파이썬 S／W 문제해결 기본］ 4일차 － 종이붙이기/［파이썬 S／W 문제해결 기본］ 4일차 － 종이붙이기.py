def paper(n):
    dp = [0] * max((n//10+1), 3)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 3

    for i in range(3, (n//10)+1):
        dp[i] = dp[i-1]+ dp[i-2]*2

    return dp[n//10]


T = int(input())
for t in range(1, T+1):
    n = int(input())
    print(f'#{t} {paper(n)}')