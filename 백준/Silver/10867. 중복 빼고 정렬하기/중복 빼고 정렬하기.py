import sys

input = lambda :sys.stdin.readline().rstrip()

n = int(input())
arr = list(set(map(int, input().split())))
arr.sort()
print(*arr, sep=' ')