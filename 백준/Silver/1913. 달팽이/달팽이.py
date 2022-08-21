drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]
n = int(input())
num = int(input())
list_a = [[0] * n for _ in range(n)]
idx_list = [0, 0]
now_i = n // 2
now_j = n // 2
now_dir = 3
for i in range(1, n * n +1):
    list_a[now_i][now_j] = i
    if i == num:
        idx_list[0] = now_i
        idx_list[1] = now_j
    now_dir = (now_dir + 1) % 4
    ni, nj = now_i + drow[now_dir], now_j + dcol[now_dir]
    if 0 <= ni < n and 0 <= nj < n and list_a[ni][nj] == 0:
        now_i, now_j = ni, nj
    else:
        now_dir = (now_dir - 1) % 4
        now_i += drow[now_dir]
        now_j += dcol[now_dir]
for line in list_a:
    print(*line)
print(idx_list[0] + 1, idx_list[1] + 1)