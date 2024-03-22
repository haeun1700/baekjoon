import sys

n = int(input())
card = [*map(int, sys.stdin.readline().split())]
b = [0] * 20000001

for i in card:
    b[i] += 1

m = int(input())
result = [*map(int, sys.stdin.readline().split())]
for i in result:
    print(b[i], end=' ')