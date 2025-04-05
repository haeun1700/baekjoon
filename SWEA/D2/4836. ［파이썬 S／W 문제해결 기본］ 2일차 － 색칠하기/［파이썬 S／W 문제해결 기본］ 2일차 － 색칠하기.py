def color_problem(r1, c1, r2, c2, color):
    cnt = 0
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            if graph[i][j] == color or graph[i][j] == '0':
                graph[i][j] = color
            else:
                graph[i][j] = color
                cnt += 1
    return cnt


T = int(input())
for t in range(1, T+1):
    graph = [['0'] * 10 for i in range(10)]
    n = int(input())
    result = 0
    for i in range(n):
        r1,c1,r2,c2,color = map(int, input().split())
        result += color_problem(r1,c1,r2,c2,color)

    print(f'#{t} {result}')