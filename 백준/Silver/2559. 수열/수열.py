n, k = map(int, input().split())
arr = list(map(int, input().split()))

window_sum = sum(arr[:k])
result = window_sum

for i in range(k, n):
    window_sum += arr[i]-arr[i-k]
    result = max(window_sum, result)

print(result)