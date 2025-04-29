n = input()
diff = int(n) - (int(n[0]) + 9*(len(n)-1))

for i in range(diff, 1000001):
    result = i + sum(map(int, str(i)))
    if result == int(n):
        print(int(i))
        break
else:
    print(0)