import sys
input = lambda: sys.stdin.readline()

def count_digits(n):
    length = 0
    digit =1
    start = 1

    while start * 10 <= n:
        length += digit * (start * 9)
        start *= 10
        digit += 1

    length += digit * (n - start + 1)
    return length


n = int(input())
sys.stdout.write(str(count_digits(n)))