# 졸업 요건 : 전공 3.3 이상 or 졸업고사 통과
# 전공과목별 학점 * 평점의 합 // 학점 총합

dic = {"A+": 4.5, "A0": 4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, "D+": 1.5, "D0":1.0, "F": 0}
score_total = 0
subject = 0
for t in range(20):
    a,b,c = map(str, input().split())
    b = int(b[0])

    if c == 'P':
        continue
    score_total += dic[c] * b
    subject += b

print("{:.6f}".format(score_total / subject))