def factorial(n):
    if n == 0:
        return 1
    else:
        total = 1
        for n in range(n, 1, -1):
            total *= n
        return total


print(factorial(int(input())))
