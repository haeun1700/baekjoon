# 7을 가져가야해 현재 총길이의 중간값을 구하고 이것을 다 빼주고 더했어


import sys
input = lambda: sys.stdin.readline().rstrip()

k,n = map(int, input().split())
arr = list()
for i in range(k):
    arr.append(int(input()))

start = 1
end = max(arr)
result = 0
while start <= end:
    mid = (start + end) // 2

    sum = 0
    for i in arr:
        sum += 0 if i//mid < 0 else i // mid
    if sum >= n:
        start = mid+1
    else:
        end = mid-1

print(end)