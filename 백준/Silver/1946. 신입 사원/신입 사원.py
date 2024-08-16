import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    candidates = []
    n = int(input())
    for _ in range(n):
        s,m = map(int, input().split())
        candidates.append((s,m))

    candidates.sort()

    top_ranking = 1e9
    count = 0
    
    for i in range(n):
        if candidates[i][1] < top_ranking:
            count += 1
            top_ranking = candidates[i][1]

    print(count)