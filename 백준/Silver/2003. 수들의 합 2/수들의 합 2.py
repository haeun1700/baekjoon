# N개의 수로 된 수열  , 4개의 수열의 합이 m이 되는 경우의 수
n, m = map(int, input().split())
A = list(map(int, input().split()))

start = 0
end = 0
res = A[0]

count = 0
while True:
    if res == m:
        count += 1
    if res >= m:
        res -= A[start]
        start += 1
    else:
        if end == n-1:
            break
        end += 1
        res += A[end]

print(count)