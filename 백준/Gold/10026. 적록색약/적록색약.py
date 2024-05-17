import sys
from queue import Queue
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
graph = []
q = Queue()
visited = [[0] * N for _ in range(N)]
for _ in range(N):
    graph.append(list(map(str, input())))

dx = [0,0,-1,1] #x를 가로, y를 세로
dy = [-1,1,0,0]
def dfs(i, j):
    visited[i][j] = 1
    color = graph[i][j]
    for k in range(4):
        nx = dx[k] + j
        ny = dy[k] + i
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        if visited[ny][nx] == 0 and graph[ny][nx] == color:
            dfs(ny, nx)

# #상하좌우가 빨 파 그 일때
count = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i,j)
            count +=1

visited = [[0] * N for _ in range(N)]
count_two = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            dfs(i,j)
            count_two +=1

print(count, count_two)