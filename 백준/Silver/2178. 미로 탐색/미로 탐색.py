import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def maze_search(rows, cols, maze):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or maze[nx][ny] != 1:
                continue

            q.append((nx, ny))
            maze[nx][ny] = maze[x][y] + 1


    return maze[rows-1][cols-1]

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
print(maze_search(n, m, arr))
