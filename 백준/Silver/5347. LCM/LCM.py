def GCD(n, m):
    # 8 12  12 4  -> 4 0
    # 8 4
    if m != 0:
        return GCD(m, n % m)

    else:
        return n


def LCM(n, m):
    return n * m // GCD(n, m)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        print(LCM(a, b))
