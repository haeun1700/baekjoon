import sys
n = int(input())
line = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
line_ = 0
line.sort(key=lambda x: x[0])
start = line[0][0]
end = line[0][1]
for i in range(1, n):
    if line[i][0] > end:
        line_ += (end - start)
        start = line[i][0]
        end = line[i][1]

    else:
        end = max(end, line[i][1])
print(line_+(end-start))
