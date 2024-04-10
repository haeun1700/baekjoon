import sys

input = lambda : sys.stdin.readline()
n,m= map(int, input().split())
s = [input() for _ in range(n)]
e = [input() for _ in range(m)]
count = 0
for i in e:
    if i in s:
        count += 1
print(count)