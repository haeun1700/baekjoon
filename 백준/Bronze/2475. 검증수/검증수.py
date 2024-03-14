n = list(map(int, input().split()))
m = 0
for i in n:
    m += i ** 2
print(m % 10)
