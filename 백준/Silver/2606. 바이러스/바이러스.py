n = int(input())
m = int(input())
graph = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)
count = 0

for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1


def virus(v):
    global count
    visited[v] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            virus(i)


virus(1)
print(sum(visited)-1)