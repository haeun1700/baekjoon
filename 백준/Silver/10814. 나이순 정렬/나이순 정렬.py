n = int(input())
arr = []
for i in range(n):
    age, name = map(str, input().split())
    arr.append([int(age), name])

sorted_dic = sorted(arr, key=lambda x: x[0])
for age, name in sorted_dic:
    print(age, name)
