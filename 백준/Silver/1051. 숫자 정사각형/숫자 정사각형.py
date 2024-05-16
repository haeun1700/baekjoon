import sys
input = lambda: sys.stdin.readline()

n,m = map(int, input().split())

arr = [list(map(int, input().rstrip())) for i in range(n)]

size = 1
for i in range(0, n):
    for j in range(0, m):
        k = 1 # 정사각형 체크
        while k < min(n, m):
            if i + k >= n or j + k >= m: # 정사각형 범위를 벗어났을 경우
                break
            if arr[i][j] == arr[i][j+k] and arr[i][j] == arr[i+k][j] and arr[i][j] == arr[i+k][j+k]:
                size = max((k + 1) * (k + 1), size)
            k += 1
print(size)