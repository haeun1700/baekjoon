import sys

input = lambda :sys.stdin.readline().rstrip()

n= int(input())
arr = [int(input()) for i in range(n)]
arr.sort()
print(*arr, sep="\n")