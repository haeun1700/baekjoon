
t = int(input())
for i in range(1, t+1):
    a = list(map(int, input().split()))
    total = 0
    for j in a:
        if j % 2 != 0:
            total += j
    print("#", end='')
    print(i, total)
            