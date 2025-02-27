n, m = map(int, input().split())
running_time = list(map(int, input().split()))

left = max(running_time) # 강의를 하나씩만 담을 수 있을정도로 블루레이가 충분하다면 최소값은 강의의 max값
right = sum(running_time) # 강의를 다 묶으면, 최대 담을 수 있는 용량이 됨.

while left <= right:
    mid = (left+right) // 2

    blueray_num = 1
    remain = mid
    # 남아있는 저장소 remain이 담을 강의 길이보다 작다면 blueray 1 증가, remain은 다시 리셋
    for i in range(n):
        if remain < running_time[i]:
            blueray_num += 1
            remain = mid

        remain -= running_time[i]
    # 다 돌고 블루레이가 남거나 같으면 정답으로 값 담고, 담을 용량이 크기에 1 감소
    if blueray_num <= m:
        answer = mid
        right = mid-1
    else:  # 블루레이가 주어진 갯수보다 크다면 용량이 작기에 1증가
        left = mid + 1

print(answer)