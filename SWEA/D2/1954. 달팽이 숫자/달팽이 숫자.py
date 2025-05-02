T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    x,y = 0,0
    v = 1

    dx = [0, 1, 0, -1]# 오른쪽, 아래, 왼쪽, 위
    dy = [1, 0, -1, 0]
    index = 0
    arr[0][0] = 1

    while v < n*n:
        if index == 4:
            index = 0
        nx = x + dx[index]
        ny = y + dy[index]

        if 0 <= nx and nx < n and 0 <= ny and ny < n and arr[nx][ny] == 0:
            v += 1
            arr[nx][ny] = v
            x,y = nx,ny

        elif x == n:
            index += 1
            x -= 1
        elif x < 0:
            index += 1
            x += 1
        elif y == n:
            index += 1
            y -= 1
        elif y < 0:
            index += 1
            y += 1

        else:
            index += 1

    print(f'#{t}')
    for i in arr:
        print(*i)