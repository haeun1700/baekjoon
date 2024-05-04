# import sys
# input = sys.stdin.readline
#
# n = int(input())
# # 시작 시간, 종료 시간 정렬
# # 정렬된 리스트 순서대로 실행 if 끝나는 시간 > 시작시간 강의실 하나 추가
#
# 2 14   1
# 3  8   1  12 18  20 25
# 6  20   1
# 6  27   1
# 7  13   1  15  21

import heapq
import sys

input = lambda: sys.stdin.readline()
n = int(input())
h= []

for i in range(n):
    num = int(input())
    if num == 0:
        if len(h) == 0: print(0)
        else:
            print(heapq.heappop(h))
    else:
        heapq.heappush(h, num)