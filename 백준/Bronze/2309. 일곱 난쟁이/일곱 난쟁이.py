from itertools import combinations
import sys
input = sys.stdin.readline

person = []
for _ in range(9):
    k = int(input())
    person.append(k)

for answer in combinations(person, 7):
    if sum(answer) == 100:
        answer = list(answer)
        answer.sort()
        for i in answer:
            print(i)
        break