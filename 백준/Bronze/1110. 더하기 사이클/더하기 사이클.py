import sys

input = lambda:sys.stdin.readline()
n = int(input())
temp = n
cnt = 0
while True:
    # 1. 현재 값 각 자리수 합
    sum_num = (temp//10) + (temp % 10)
    # 2. str(기존값의 맨 마지막 자리 수) + str(자리수합의 오른쪽 자리)
    new_num = str(temp % 10) + str(sum_num % 10)
    temp = int(new_num)
    # 3.그리고 그 새로운 수가 초기 값과 같은지 체크
    cnt += 1
    if temp == n:
        break

print(cnt)