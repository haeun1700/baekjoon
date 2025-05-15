n, jimin, hans = map(int, input().split())
round = 0

while jimin != hans:
    round += 1
    jimin = (jimin+1)//2 # 다음 경기에서의 내 번호는 +1 후 나누기 2하면 된다.
    hans = (hans+1)//2

print(round)