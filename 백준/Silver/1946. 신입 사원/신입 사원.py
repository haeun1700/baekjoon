import sys

input = lambda :sys.stdin.readline().rstrip()

t = int(input())
a = []
b = []
for _ in range(t):
    n = int(input())
    people = [list(map(int, input().split())) for _ in range(n)]
    people.sort(key=lambda x: x[0])
    cnt = 1
    temp = people[0][1]
    for i in range(1,n):
        if people[i][1] < temp:
                # 어차피 면접 기존 temp에 있는 점수는 비교해도 못이기기 때문에 temp를 리뉴얼하여 얘를 이기면 이기게 됨.
                temp = people[i][1]
                cnt += 1
    print(cnt)