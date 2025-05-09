n,k = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
total = 0
result = []
cnt = 0

while True:
    if end == n:
        result.append(total)
        break

    elif cnt >= k:
        result.append(total)
        total -= arr[start]
        start += 1
        cnt -= 1
    elif cnt < k:
        total += arr[end]
        end += 1
        cnt += 1


print(max(result))