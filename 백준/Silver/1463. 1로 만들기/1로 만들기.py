n = int(input())
dp = [0 for _ in range(n+1)]
#1을 i로 만든느데 필요한 최소 연산의 수를 구하는 문제
#이미 i가 1이므로 연산횟수 0
def dp_(n):
    for i in range(2,n+1):
        if i % 6 == 0:
            dp[i] = min(dp[i//3], dp[i//2], dp[i-1]) + 1
        elif i % 3 == 0:
            dp[i] = min(dp[i//3], dp[i-1])+1
        elif i % 2 == 0:
            dp[i] = min(dp[i//2], dp[i-1])+1
        else:
            dp[i] = dp[i-1] +1

    return dp[n]


print(dp_(n))