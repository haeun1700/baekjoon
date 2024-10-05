def island_count(cols, rows,graph): # 0 1 1 0

    dx = [-1,1,0,0,-1,-1,1,1]
    dy = [0,0,-1,1,-1,1,-1,1]
    cnt = 0

    for row in range(rows): # 0
        for col in range(cols): # 0 1
            if graph[row][col] != 1:
                continue

            stack = [(row, col)] # 0 1
            cnt += 1 # 1
            while stack:
                x,y = stack.pop() # 0 1
                # print("while", x,y)
                graph[x][y] = 0 # 방문처리
                for i in range(8):
                    nx = dx[i] + x #
                    ny = dy[i] + y
                    if nx >= rows or ny >= cols or nx < 0 or ny < 0 or graph[nx][ny] != 1:
                        continue

                    stack.append((nx, ny))

    return cnt


while True:
    w, h = map(int, input().split()) # 2 2
    if w == 0 and h == 0:
        exit(0)
    graph = [list(map(int, input().split())) for _ in range(h)]
    print(island_count(w, h,graph))