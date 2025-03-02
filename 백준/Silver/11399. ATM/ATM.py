# i번 사람이 돈을 인출하는데 걸리는 시간 Pi분, 필요한 시간 최솟값 구하기
# 1 2 3 4 5
# 3 1 4 3 2
# 그리디, 18분 소요
import sys
input = lambda: sys.stdin.readline()

n = int(input())
P = list(map(int, input().split())) #
# 앞 사람이 빨리 끝날수록 필요한 시간이 최솟값이 된다 -> 정렬
P.sort()
res = 0
for i in range(n):
    res += P[i]
    P[i] = res

print(sum(P))