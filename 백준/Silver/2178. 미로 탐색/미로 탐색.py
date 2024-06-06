from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
count = 0

def bfs(x,y):
    visited[x][y] = 1
    q = deque()
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <0 or ny <0 or nx >=n or ny>= m:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] ==0:
                q.append((nx,ny))
                visited[nx][ny] = 1
                graph[nx][ny] = graph[x][y] + 1


bfs(0,0)
print(graph[n-1][m-1])