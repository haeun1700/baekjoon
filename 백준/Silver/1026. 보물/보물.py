import sys
import heapq
input = lambda: sys.stdin.readline()
#temp에 b 가 작은수부터 정렬된 값을 dic에 담아
# 출력 시 해당 b의 키 값에 값을 곱하고 총합을 두해
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

B.sort()
A.sort(reverse=True)

total = 0
j = 0
for i in B:
    total += i*A[j]
    j += 1
print(total)