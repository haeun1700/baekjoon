from itertools import permutations
import sys
input = sys.stdin.readline

# 모든 가능한 순서, 차이의 합 일일이 구하고 출력
n = int(input())
arr = list(map(int, input().split()))

result = 0
for i in permutations(arr, n):
    diff_sum = 0
    for j in range(n-1):
        diff_sum += abs(i[j] - i[j+1])

    if diff_sum >= result:
        result = diff_sum

print(result)