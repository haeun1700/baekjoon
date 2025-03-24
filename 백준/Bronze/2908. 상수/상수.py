A,B = map(str, input().split())
new_A = ''
new_B = ''
for i in range(2, -1, -1):
    new_A += A[i]
    new_B += B[i]

print(int(new_A) if int(new_A) > int(new_B) else int(new_B))