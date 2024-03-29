import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
m = [*map(int, input().split())]
cnt = 0
b = {}
for i in sorted(m):
    if i not in b:
        b[i] = cnt
        cnt += 1
for i in m:
    print(b[i], end =' ')
