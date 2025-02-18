import itertools

n = int(input())
people = []
for i in range(n):
    arr = list(map(int, input().split()))
    people.append(arr)

# 5장 중에서 3개의 조합,
# 그 조합 합 중에서 일의 자리가 큰 수 선택
result = []
for i in range(len(people)):
    sum_max = list(itertools.combinations(people[i], 3))
    ans = -1e9
    for j in sum_max:
        ans = max(ans, (sum(j)%10))
    result.append(ans)

max_val = max(result)
print(max(i for i,v in enumerate(result) if v == max_val)+1)