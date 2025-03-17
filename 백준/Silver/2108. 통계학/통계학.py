from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
Li = sorted(int(input()) for _ in range(N))

tmp = Counter(Li)
max_tmp = max(tmp.values())
mode = [key for key, value in tmp.items() if value == max_tmp]

print(round(sum(Li) / N))  # 평균값
print(Li[N // 2])  # 중앙값

if len(mode) > 1:  # 최빈값
    print(mode[1])

else:
    print(mode[0])

print(max(Li) - min(Li))  # 범위