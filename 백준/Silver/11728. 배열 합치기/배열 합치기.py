import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
result = a+b
result.sort()
print(*result)
