import sys
input = lambda : sys.stdin.readline().strip()

t = int(input())
for _ in range(t):
    a = input().split()
    temp = []
    for i in a:
        temp.append(i[::-1])
    print(' '.join(temp))