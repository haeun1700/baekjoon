import sys
import heapq
input = lambda: sys.stdin.readline()


t = int(input())

for _ in range(t):
    k = int(input())
    k_list = list(map(int, input().split()))
    h = []
    total = 0
    for i in k_list:
        heapq.heappush(h, i)

    while len(h) > 1:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        heapq.heappush(h, a+b)
        total += a+b

    print(total)