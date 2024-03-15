while True:
    n = list(map(int, input().split()))
    n.sort()
    a = n[0]
    b = n[1]
    c = n[2]

    result = a ** 2 + b ** 2
    if a == b == c == 0:
        exit()
    elif result == c ** 2:
        print("right")
    else:
        print("wrong")
