n = int(input())
days = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n+1)

for i in range(n):
    T, P = days[i]
    # 상담 했을 때
    if i+T<=n:
        dp[i+T] = max(dp[i+T], dp[i]+P) # 현재 값 vs 상담하고 왔을 때의 값
    # 상담 안했을 떄
    dp[i+1] = max(dp[i+1], dp[i])

print(max(dp))