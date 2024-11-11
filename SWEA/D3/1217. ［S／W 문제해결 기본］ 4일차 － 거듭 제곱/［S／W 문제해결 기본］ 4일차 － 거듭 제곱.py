def func(res, num):
    res *= num
    return res


for _ in range(10):
    t = int(input())
    n,m = map(int, input().split())
    result = n
    for i in range(m-1):
        result = func(result, n)
    print(f'#{t} {result}')
    
