n = int(input())
meetings = []
# 끝나는 시간을 기준으로 정렬하기
for _ in range(n):
    start, end = map(int, input().split())
    meetings.append((start, end))
meetings.sort(key=lambda x: (x[1], x[0]))

count = 1
end = meetings[0][1]
for i in range(1,n):
    if meetings[i][0] >= end:
        end = meetings[i][1]
        count += 1
print(count)
