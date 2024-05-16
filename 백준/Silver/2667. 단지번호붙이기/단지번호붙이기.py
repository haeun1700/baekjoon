dx = [0,0,1,-1]
dy = [-1,1,0,0]
n = int(input())

visited = [[0] * n for _ in range(n)]
arr = []
count = 0
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

def dfs(x,y):
    visited[x][y] = 1
    global count
    count += 1
    for i in range(4):
        nx = x + dy[i]
        ny = y + dx[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        if graph[nx][ny] == 1 and visited[nx][ny] == 0:
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            dfs(i, j)
            arr.append(count)
            count = 0

print(len(arr))
for i in sorted(arr):
    print(i)