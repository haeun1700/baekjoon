n,m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 0
total = 0
cnt = 0
result = []

while True:
    if total >= m:
        result.append(right-left)
        total -= arr[left]
        left += 1

    elif right < n:
        total += arr[right]
        right += 1

    else:
        break

print(min(result) if result else 0)