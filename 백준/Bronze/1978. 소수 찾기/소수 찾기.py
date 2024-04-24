import math

n = input()
n_ = list((map(int, input().split())))
cnt = 0
for i in n_:
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        cnt += 1

print(cnt)
