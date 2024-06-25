c = int(input())

for _ in range(c):
    score = list(map(int, input().split()))
    avg = (sum(score[1:])) / score[0] # 200+ 150 = 350 // 5 = 70 -> 3명, 2/5 =
    cnt = 0
    for i in score[1:]:
        if i > avg:
            cnt += 1
    result = (cnt / score[0]) * 100
    print("{:.3f}".format(result), '%', sep='')
