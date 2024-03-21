import sys

n = int(input())
person = []
for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    person.append((int(age), name))
# 이름으로 정렬. i[0]과 i[1]출력*
for i in sorted(person, key=lambda x: x[0]):
    print(i[0], i[1])