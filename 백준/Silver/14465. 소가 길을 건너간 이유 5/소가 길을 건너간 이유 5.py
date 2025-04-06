import sys
input = lambda: sys.stdin.readline()

n, k, B = map(int, input().split())
a = [0] * n

for _ in range(B):
    b = int(input())
    a[b-1] = -1

result = 1e9
aa = 0
for i in range(n-k+1):
    cnt = 0
    for j in range(i, i+k):
        if a[j] == -1:
            cnt += 1
    result = min(cnt, result)

print(result)