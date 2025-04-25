n = int(input())
dp = [[0] * (n+1) for _ in range(n+1)]
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n+1):
    for j in range(1, len(graph[i-1])+1):
        dp[i][j] = graph[i-1][j-1] + max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[n]))