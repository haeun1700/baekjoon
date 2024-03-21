
import sys

n = int(sys.stdin.readline())
arr_n = []
for i in range(n):
    arr_n.append(int(sys.stdin.readline()))

arr_n.sort()
for j in arr_n:
    print(j)