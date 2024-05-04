import sys
input = sys.stdin.readline

n = int(input())
time = list(map(int, input().split()))
time.sort()

time_sum = 0
# 1 2 3 3 4
count = 1
for i in range(n):
    if i == 0:
        time[i] = time[i]

    else:
        time[i] = time[i] + time[i-1]

total = sum(time)
print(total)