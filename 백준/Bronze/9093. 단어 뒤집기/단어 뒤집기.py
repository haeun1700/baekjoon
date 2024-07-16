import sys
input = lambda : sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    a = input().split(' ')
    for i in a:
        temp = i[::-1]
        print(temp, end=' ')