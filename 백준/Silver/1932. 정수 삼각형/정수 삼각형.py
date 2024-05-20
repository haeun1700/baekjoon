n = int(input())
dp = [[0] * n for _ in range(n)]
a = [list(map(int, input().split())) for _ in range(n)]
dp[0][0] = a[0][0]

def dp_triangle():
    for i in range(1, n):
        for j in range(0, i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + a[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + a[i][j]

    return max(dp[n-1])


print(dp_triangle())