import sys
from collections import deque

input = lambda : sys.stdin.readline()

q = deque()
n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque([[x,y]])
    visited[x][y] = 1
    color = graph[x][y]

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] == color:
                q.append([nx,ny])
                visited[nx][ny] = 1

def get_cnt():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i, j)
                cnt += 1

    return cnt


print(get_cnt(), end=' ')
visited = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

print(get_cnt())
