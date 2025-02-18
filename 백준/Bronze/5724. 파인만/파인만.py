while True:
    n = int(input())
    if n == 0:
        break

    answer = 0
    for i in range(n):
        for j in range(n):
            answer += min(n-i, n-j)
    print(answer)