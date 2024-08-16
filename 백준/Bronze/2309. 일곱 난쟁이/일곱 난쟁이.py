from itertools import combinations
import sys

input = sys.stdin.readline

nanjang = []
for _ in range(9):
    k = int(input())
    nanjang.append(k)

for i in combinations(nanjang, 7):
    if sum(i) == 100:
        for result in sorted(i):
            print(result)
        break