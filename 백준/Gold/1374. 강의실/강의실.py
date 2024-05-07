import sys
import heapq
input = sys.stdin.readline

n = int(input())
# 시작 시간, 종료 시간 정렬
# 정렬된 리스트 순서대로 실행 if 끝나는 시간 > 시작시간 강의실 하나 추가
meetings = []
for _ in range(n):
    num, start, end = map(int, input().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[0], x[1]))

h = []
heapq.heappush(h, meetings[0][1])

for i in range(1, n):
    if meetings[i][0] < h[0]:
        heapq.heappush(h, meetings[i][1])
    else:
        heapq.heappop(h)
        heapq.heappush(h, meetings[i][1])

print(len(h))
