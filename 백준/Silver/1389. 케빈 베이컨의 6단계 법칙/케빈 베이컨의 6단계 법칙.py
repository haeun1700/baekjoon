import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]


# 연결요소 체크
for _ in range(1, m+1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


result = []
count = 0
min_kevin_bacon = 1e9
min_person = -1
# 방문 처리
for i in range(1, n+1):
    visited = [False] * (n + 1)
    dist = [-1] * (n+1)

    queue = deque([i])
    visited[i] = True
    dist[i] = 0

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                dist[v] = dist[u] + 1

    kevin_bacon = sum(dist)
    if min_kevin_bacon > kevin_bacon:
        min_kevin_bacon = kevin_bacon
        min_person = i

print(min_person)