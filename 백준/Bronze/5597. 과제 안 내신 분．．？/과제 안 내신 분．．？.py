arr = [int(input()) for i in range(28)]
arr.sort()

for i in range(1,31):
    if i not in arr:
        print(i)