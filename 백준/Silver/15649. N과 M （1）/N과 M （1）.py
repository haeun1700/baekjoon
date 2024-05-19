n, m = list(map(int, input().split()))
ans = []

def backtracking():
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(1, n+1):
        if i not in ans:
            ans.append(i)
            backtracking()
            ans.pop()

backtracking()