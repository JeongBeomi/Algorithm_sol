list_a = [list(map(int, input().split())) for _ in range(9)]
max_idx = [0, 0]

for i in range(9):
    for j in range(9):
        if list_a[max_idx[0]][max_idx[1]] < list_a[i][j]:
            max_idx[0] = i
            max_idx[1] = j
print(list_a[max_idx[0]][max_idx[1]])
print(max_idx[0] + 1, max_idx[1] + 1)