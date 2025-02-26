n = int(input())
request_price = list(map(int, input().split()))
total_price = int(input())
request_price.sort()
# 적절한 상한액을 찾으려면 이분 탐색이 필요.
# 30 40 70 80 100=> mid = 0+150 // 2
left = 0
right = request_price[-1]
answer = 0
cnt = 0
while left <= right:
    mid = (left + right) // 2
    res = 0
    for i in request_price:
        res += min(i, mid)
    if total_price < res:
        right = mid - 1
    elif total_price > res:
        left = mid + 1
        answer = mid
    else:
        answer = mid
        break

print(answer)