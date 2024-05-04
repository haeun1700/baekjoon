import heapq
import sys

input = lambda: sys.stdin.readline()
n = int(input())
h= []

for i in range(n):
    num = int(input())
    if num > 0:
        heapq.heappush(h, -num)
    elif num == 0:
        if len(h) == 0: print(0)
        else:
            print(-heapq.heappop(h))