n = int(input())
n_ = list((map(int, input().split())))
max_ = max(n_)
sum_ = 0
avg = 0
for i in n_:
    sum_ += (i / max_) * 100
    avg = sum_ / len(n_)

print(avg)
