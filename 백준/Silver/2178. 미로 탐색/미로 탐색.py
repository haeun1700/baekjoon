import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
graph = []
visited = [[0] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append([x,y])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append([nx, ny])
                graph[nx][ny] = graph[x][y] +1
                visited[nx][ny] = 1

    return graph[n-1][m-1]


print(bfs(0,0))