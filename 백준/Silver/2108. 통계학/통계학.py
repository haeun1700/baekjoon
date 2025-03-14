# n개의 수를 대표하는 기본 통계값
# 4가지 통계값 구하기
import sys
input = lambda :sys.stdin.readline()
n = int(input())

# n개의 정수
arr = [int(input()) for i in range(n)]
arr.sort()
dic = {}
for i in arr:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
dic_sorted = sorted(dic.items(), key=lambda x: x[1], reverse=True)
# max_value = dic_sorted[0][0]
# second_value = -1e9


result = max(dic, key=dic.get)
print(round(sum(arr) / n)) # 산술
print(arr[(n//2)]) # 중앙

if n == 1:
    print(dic_sorted[0][0])
else:
    if dic_sorted[0][1] == dic_sorted[1][1]:
        print(dic_sorted[1][0])
    else:
        print(dic_sorted[0][0])
# print(max_value if n == 1 else max(max_value, second_value))
print(arr[-1] - arr[0])

