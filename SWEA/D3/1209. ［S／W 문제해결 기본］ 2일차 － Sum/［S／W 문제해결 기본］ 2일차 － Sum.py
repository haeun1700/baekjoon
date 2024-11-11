for _ in range(10):
    t = int(input())
    arr = [list(map(int, input().split())) for i in range(100)]
    col_list = []
    row_list = []
    right_sum = 0
    left_sum = 0
    result = 0
    for i in range(100):
        row_list.append(sum(arr[i]))
        col_sum = 0
        for j in range(100):
            col_sum += arr[j][i]
        col_list.append(col_sum)
        right_sum += arr[i][i]
        left_sum += arr[i][99-i]

    result = max(max(col_list), max(row_list), right_sum, left_sum)
    print(f'#{t} {result}')
    
    
    