t = int(input())

map_list = [[0] * 100 for _ in range(100)]
overlap_cnt = 0
for tc in range(t):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if map_list[i][j]:
                overlap_cnt += 1
                continue
            map_list[i][j] = 1
print(f"{100 * t - overlap_cnt}")
