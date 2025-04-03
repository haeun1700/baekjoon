T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    max_value = sum(arr[:m])
    min_value = sum(arr[:m])

    for i in range(n-m+1):
        diff = sum(arr[i:i+m])
        if max_value <= diff:
            max_value = diff

        if min_value >= diff:
            min_value = diff

    print(f'#{t} {max_value-min_value}')