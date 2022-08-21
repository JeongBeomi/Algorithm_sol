drow = [1, 0, -1, 0]
dcol = [0, 1, 0, -1]

c, r = map(int, input().split())
num = int(input())

list_a = [[0] * c for _ in range(r)]
now_i, now_j = 0, 0
now_dir = 0
idx_list = [0, 0]

if c * r < num:
    print(0)
else:
    for i in range(1, c * r + 1):
        list_a[now_i][now_j] = i

        if i == num:
            idx_list[0] = now_i
            idx_list[1] = now_j
            break

        ni, nj = now_i + drow[now_dir], now_j + dcol[now_dir]
        if 0 <= ni < r and 0 <= nj < c and list_a[ni][nj] == 0:
            now_i, now_j = ni, nj
        else:
            now_dir = (now_dir + 1) % 4
            now_i += drow[now_dir]
            now_j += dcol[now_dir]

    print(idx_list[1] + 1, idx_list[0] + 1)