import heapq, sys

input = lambda: sys.stdin.readline()
n = int(input())
arr = []

for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(arr, num)
    else:
        print(heapq.heappop(arr) if len(arr) > 0 else 0)