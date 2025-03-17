from collections import deque
import sys
input = lambda :sys.stdin.readline() # 시간 초과 발생해서 추가해봄
def bfs_que(graph):
    q = deque()
    visited = [False] * (n+1)
    cnt = 0

    for i in range(1, n+1):
        if visited[i]:
            continue
        q.append(i)
        cnt += 1
        
        while q:
            node = q.popleft()

            for i in graph[node]:
                if visited[i]:
                    continue
                q.append(i)
                visited[i] = True

    return cnt


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(bfs_que(graph))
