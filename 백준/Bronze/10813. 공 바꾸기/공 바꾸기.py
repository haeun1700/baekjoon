n, m = map(int, input().split())
bags = list(range(n+1))
# 0 1 2 3 4 5
for t in range(m):
    i, j = map(int, input().split())
    bags[i], bags[j] = bags[j], bags[i]

print(*bags[1:], end=' ')