n = int(input())
cnt = n
for i in range(n):
    word = input()
    visited = [0] * 1000
    for s in range(len(word)):
        check = ord(word[s])
        if visited[check] == 0:
            visited[check] = 1
        else:
            if word[s-1] == word[s]:
                continue
            else:
                cnt = cnt - 1
                break
print(cnt)