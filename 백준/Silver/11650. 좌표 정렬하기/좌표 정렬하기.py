import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    arr.append([x, y])

arr.sort(key=lambda z: (z[0], z[1]))

for i in arr:
    print(i[0], i[1])