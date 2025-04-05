word = input()
arr = []
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        a, b, c = word[:i], word[i:j], word[j:]
        result = a[::-1] + b[::-1] + c[::-1]
        arr.append(result)

arr.sort()
print(arr[0])