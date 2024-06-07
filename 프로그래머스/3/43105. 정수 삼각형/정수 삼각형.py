def solution(triangle):
    answer = 0
    n = len(triangle)-2
    for i in range(n, -1, -1):
        m = len(triangle[i])-1
        for j in range(m, -1, -1):
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j+1])
    
    return triangle[0][0]