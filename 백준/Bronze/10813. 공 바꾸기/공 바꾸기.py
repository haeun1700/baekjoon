# n개의 바구니, 1~n번까지 번호가 매겨져있다.
# 1번 바구니 -> 1번 공
# m번 공을 바꾼다 ->

n, m = map(int, input().split())
bags = [i for i in range(n+1)]
# 0 1 2 3 4 5
for t in range(m):
    i, j = map(int, input().split())
    temp = bags[i]
    bags[i] = bags[j]
    bags[j] = temp

print(*bags[1:], end=' ')