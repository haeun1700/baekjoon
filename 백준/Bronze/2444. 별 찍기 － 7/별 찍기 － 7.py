n = int(input())

cnt = 0
for i in range(1, (n*2)+1):
    # 공백4, 별1개, 공백 3개 별 3개
    print(' ' * abs(n-i),end='')
    if i >= n:
        print('*' * (((n*2) - i)*2-1))
    else:
        print('*' * (i*2-1))