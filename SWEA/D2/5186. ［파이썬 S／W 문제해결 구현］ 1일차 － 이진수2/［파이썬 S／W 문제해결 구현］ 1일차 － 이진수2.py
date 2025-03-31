T = int(input())
for t in range(1, T+1):
    n = float(input())
    result = ''

    while n != 0:
        n *= 2
        integer_num = int(n)
        result += str(integer_num)
        decimal_num = n - integer_num
        n = decimal_num
        if len(result) >= 13:
            result = 'overflow'
            break
    print(f'#{t} {result}')