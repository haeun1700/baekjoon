# 길이가 m인 회문 찾기
# 길이가 정해져 있네. 그럼 그 시작 i에 + m까지 하고 이를 슬라이싱 처리 -> 반대 뒤집어서 같으면 출력
T = int(input())

def col_dense(graph, n):
    new_graph = []
    for i in range(n):
        word = ''
        for j in range(n):
            word += graph[j][i]
        new_graph.append(list(word))
    return new_graph


for t in range(1, T+1):
    n, m = map(int, input().split())
    graph = [list(map(str, input())) for i in range(n)]
    new_graph = col_dense(graph, n)
    for i in range(n):
        for j in range(n-m+1):
            word1 = graph[i][j:j+m]
            word2 = new_graph[i][j:j+m]
            if word1 == word1[::-1]:
                print(f"#{t} {''.join(word1)}")
                break
            elif word2 == word2[::-1]:
                print(f"#{t} {''.join(word2)}")
                break


