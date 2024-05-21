
def solution(clothes):
    d = {}
    for v in clothes:
        if not v[1] in d:
            d[v[1]] = 1
        else:
            d[v[1]] += 1
    ans = 1
    for i in d.keys():
        ans *= d[i] + 1
    return ans - 1