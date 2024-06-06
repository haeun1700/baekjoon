from collections import deque
             
    
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((0,0))
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx>=n or ny >=m:
                continue
            if maps[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
                maps[nx][ny] = maps[x][y]+1
                
    if maps[n-1][m-1] <= 1:
        return -1
    
    return maps[n-1][m-1]
