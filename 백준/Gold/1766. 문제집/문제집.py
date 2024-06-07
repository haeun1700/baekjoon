import heapq

def TS_indegree(graph, n):
    result = []
    queue = []
    indegree = [0] * n
    for i in range(n):
        for j in graph[i]:
            indegree[j] += 1
    for i in range(n):
        if indegree[i] == 0:
            heapq.heappush(queue, i)
    while queue:
        v = heapq.heappop(queue)
        result.append(v+1)
        for j in graph[v]:
            indegree[j] -= 1
            if indegree[j] == 0:
                heapq.heappush(queue, j)
    return result


n,m= map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a-1].append(b-1)
print(*TS_indegree(graph, n))