import sys

n = int(sys.stdin.readline())
m = [int(sys.stdin.readline()) for i in range(n)]
m.sort()
for i in m:
    print(i)