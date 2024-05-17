import sys
sys.setrecursionlimit(10**6)
dx = [0,0, -1,1]
dy = [-1, 1, 0, 0]
T = int(input())


def dfs(a, b):
    visited[a][b] = 1
    for i in range(4):
        na = a+ dy[i]
        nb = b+ dx[i]
        if na < 0 or nb < 0 or nb >= m or na >= n:
            continue
        if graph[na][nb] == 1 and visited[na][nb] == 0:
            dfs(na, nb)


for _ in range(T):
    m, n, k = map(int, input().split()) #가로m, 세로n, 위치의 개수 k
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x,y = map(int, input().split())
        graph[y][x] = 1
    visited = [[0] * m for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                count += 1
    print(count)