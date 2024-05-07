import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    start, end = map(int, input().split())
    graph.append((start, end))

graph.sort(key = lambda x : (x[1], x[0]))
end = graph[0][1]
count = 1

for i in range(1, n):
    if graph[i][0] >= end:
        end = graph[i][1]
        count += 1
print(count)