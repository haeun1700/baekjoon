def vps(word):
    ps = word
    s = []
    result = "YES"
    for p in ps:
        if p == ")":
            if len(s) <= 0:
                result = "NO"
                break
            s.pop()
        if p == "(":
            s.append(p)

    if len(s)!=0: result="NO"
    return result


n = int(input())
for _ in range(n):
    ps = str(input())
    print(vps(ps))
