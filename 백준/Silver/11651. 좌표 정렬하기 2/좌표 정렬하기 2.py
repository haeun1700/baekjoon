import sys

n = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
arr.sort(key=lambda x: (x[1], x[0]))
for i in range(n):
    print(arr[i][0], arr[i][1])
