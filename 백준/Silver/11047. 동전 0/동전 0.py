import sys
input = lambda : sys.stdin.readline()

n,k = map(int, input().split())

#리스트를 정렬, 정렬한 값을 k만큼
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)
count = 0
#  첫번쨰 원소보다 크다면
for i in range(len(coins)):
    n = k // coins[i]
    if n >= 1: count += (k // coins[i])
    k = k % coins[i]
print(count)