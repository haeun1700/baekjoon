import random
t = int(input())
for _ in range(t):
    k = int(input())
    word = [input() for _ in range(k)]
    flag = 0
    palindrome = []
    for i in range(len(word)):
        for j in range(len(word)):
            if i == j: continue
            new_word = word[i] + word[j]
            if new_word == new_word[::-1]:
                flag = 1
                palindrome.append(new_word)

    print(random.choice(palindrome)) if flag == 1 else print(0)

