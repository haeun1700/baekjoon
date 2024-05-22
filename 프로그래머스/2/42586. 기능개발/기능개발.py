
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
def solution(progresses, speeds):
    answer = []
    while progresses:
        days = 1
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
        cnt = 0
        while progresses:
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                cnt += 1
            else:
                break
        if cnt:
            answer.append(cnt)
    return answer