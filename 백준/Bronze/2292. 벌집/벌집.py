n = int(input())
idx = 1
dp = {0: 0, 1: 1}
answer = 0

while True:
    if dp[idx-1] < n <= dp[idx]:
        answer = idx
        break
    idx += 1
    dp[idx] = dp[idx-1] + (6 * (idx-1))

print(answer)