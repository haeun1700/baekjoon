# n명의 후보, m명의 주민들,
# 매수해야하는 사람 최솟값 구하기
# 0< N < 50, 1< 득표수 < 100
import sys
input = lambda:sys.stdin.readline()

n = int(input())
get_arr = [int(input()) for i in range(n)]
answer = get_arr[0]
if n == 1:
    print(0)
    exit(0)
diff = max(get_arr[1:]) # 7
a = get_arr.index(diff)
cnt = 0
while diff >= answer: # 7 >= 5  7>= 6
    get_arr[get_arr.index(diff)] = diff-1
    diff -= 1 # 6 6
    answer += 1 # 6 7
    cnt += 1 # 1 2
    diff = max(get_arr[1:]) # 7 6

print(cnt)