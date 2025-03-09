n, m = map(int, input().split())
arr = [input() for i in range(n)]
# arr = [input() for i in range(1, n+1)] 이렇게 해도 파이썬 인덱스는 항상 0부터 시작한다.
dic = {arr[i] : i+1 for i in range(n)} # 1부터 시작할 수 있도록
arr2 = [input() for j in range(m)]


for i in arr2:
    # 숫자일 때-> 문자 출력
    # dic.values(i)
    if i.isdigit():
        print(arr[int(i)-1])
    # 문자일 때 -> 숫자 출력
    else:
        print(dic[i])