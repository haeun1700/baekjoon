import sys

input = lambda: sys.stdin.readline().rstrip()
total = 0
result = 0
answer = []

for i in range(10):
    n = int(input())
    total += n
    answer.append(total)

answer = sorted(answer, key=lambda x: abs(x-100))

if abs(answer[0]-100) == abs(answer[1]-100):
    print(answer[1])
else:
    print(answer[0])