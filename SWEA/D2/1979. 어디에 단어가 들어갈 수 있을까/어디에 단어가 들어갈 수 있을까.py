def row_check(n,k,puzzle):
    cnt = 0
    for row in range(n):
        length = 0
        for col in range(n):
            if puzzle[row][col] == 1:
                length += 1
            else:
                if length == k:
                   cnt += 1
                length = 0
        if length == k:
            cnt += 1
    return cnt


def col_check(n,k,puzzle):
    cnt = 0
    for col in range(n):
        length = 0
        for row in range(n):
            if puzzle[row][col] == 1:
                length += 1
            else:
                if length == k:
                    cnt += 1
                length = 0
        if length == k:
            cnt += 1
    return cnt



T = int(input())
for t in range(1, T+1):
    n,k = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{t} {row_check(n,k,puzzle) + col_check(n,k,puzzle)}')