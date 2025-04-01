# x += y 저장된 값이 n 초과, 최소 연산을 해서 n 초과되도록 계산
T = int(input())
for t in range(T):
    a, b, n = map(int, input().split())
    cnt = 0
    # n 초과되면 break
    while a <= n and b <= n:
        if a > b:
            b += a # 작은쪽에 큰 수를 더하기
        else:
            a += b
        cnt += 1

    print(cnt)