dx = [-1,1,0,0]  #x세로, y가로
dy = [0,0,-1,1]  # 상하좌우


n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
arr = []
count = 0

def dfs(x,y):
    visited[x][y] = 1
    global count
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >=n or ny >= n:
            continue
        if graph[nx][ny] == 1 and visited[nx][ny] == 0:
             dfs(nx,ny)


for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            dfs(i,j)
            arr.append(count)
            count = 0

print(len(arr))
for i in sorted(arr):
    print(i)
