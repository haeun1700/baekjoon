n = int(input())
arr = [int(input()) for _ in range(n)]
dp = [0] * max(n, 4)

dp[0] = arr[0]
if n >= 2:
    dp[1] = arr[0]+arr[1]
if n >= 3:
    dp[2] = arr[2] + max(arr[0], arr[1])
if n >= 4:
    for i in range(3,n):
        dp[i] = arr[i]+ max(dp[i-2], dp[i-3]+arr[i-1])

print(dp[n-1])