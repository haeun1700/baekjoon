n = int(input())
people = [list(map(int, input().split())) for _ in range(n)]
rank = []
for i in range(n):
    x,y = people[i][0], people[i][1]
    k = 0
    for j in range(n):
        if x < people[j][0] and y < people[j][1]:
            k += 1
    rank.append(k+1)

print(*rank, end= ' ')