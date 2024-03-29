import sys

n = int(input())
arr = [sys.stdin.readline().strip() for i in range(n)]
arr = list(set(arr))
arr.sort()
arr.sort(key=len)
for i in arr:
    print(i)