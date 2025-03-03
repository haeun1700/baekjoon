# 정렬된 숫자 카드 묶음 a, b
# 20 + 30 = 50번 비교, 그 비교가 최소가 되도록 구하기
# a + b = c  => c + d = 정답
# 1 <= n개 카드 <= 100,000 => 100억, 100초
# 앞쪽의 합이 작아야 뒤쪽의 합도 작아진다!
import heapq, sys
input = lambda:sys.stdin.readline()

n = int(input())
arr = []

for i in range(n):
    n = int(input())
    heapq.heappush(arr, n)

total = 0
res = 0
while True:
    total = 0
    if len(arr) == 1:
        print(res)
        break
    min1 = heapq.heappop(arr) #
    min2 = heapq.heappop(arr) #
    total += min1 + min2 #
    res += total
    heapq.heappush(arr,total) #