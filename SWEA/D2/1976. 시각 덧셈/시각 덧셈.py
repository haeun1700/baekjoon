T = int(input())
for t in range(1, T+1):
    a_h, a_m, b_h, b_m = map(int, input().split())
    hour, minutes = 0, 0
    hour = (a_h + b_h if (a_h + b_h) <= 12 else (a_h + b_h)-12)
    minutes = a_m+b_m
    if minutes > 59:
        hour += minutes // 60
        minutes %= 60
    print(f'#{t} {hour} {minutes}')