def backtrack(row, used, total):
    global min_total

    # 이미 합이 커졌다면 중단 (가지치기)
    if total >= min_total:
        return

    # 모든 행 다 선택했으면 최소값 갱신
    if row == n:
        min_total = min(min_total, total)
        return

    # 각 열을 하나씩 시도
    for col in range(n):
        if not used[col]:  # 아직 사용하지 않은 열
            used[col] = True
            backtrack(row + 1, used, total + arr[row][col])
            used[col] = False  # 되돌리기 (백트래킹)

T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    min_total = float('inf')
    used = [False] * n  # 열 사용 여부
    backtrack(0, used, 0)

    print(f'#{t} {min_total}')
