n = int(input())

for i in range(0, n//3+1):
    for j in range(0, n//5+1):
        if i*3+j*5 == n:
            print(i+j)
            exit(0)
print(-1)