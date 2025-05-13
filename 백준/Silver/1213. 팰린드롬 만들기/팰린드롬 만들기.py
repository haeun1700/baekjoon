# 알파벳 개수 센다 ->  홀수개가 1개 이상인지 체크 -> 알파벳 정렬 ->
# -> half만들기, center 설정
from collections import Counter

def check(n):
    cnt = 0
    for k,v in n:
        if v % 2 == 1:
            cnt += 1

    return cnt <= 1


n = input()
counter = Counter(n)
sorted_counter = sorted(counter.items(), key=lambda x:x[0])

if check(sorted_counter):
    half = ''
    center = ''

    for k,v in sorted_counter:
        if v % 2 == 1:
            center = k

        half += k * (v // 2)

    print(half + center + half[::-1])
else:
    print("I'm Sorry Hansoo")