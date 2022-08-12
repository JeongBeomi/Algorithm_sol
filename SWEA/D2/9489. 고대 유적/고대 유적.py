t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(n)]
    max_size = 2
    max_cnt = 0
    for i in range(n):
        cnt = 0
        if total_map[i].count(1) > max_size:
            for j in range(m):
                if total_map[i][j] == 1:
                    cnt += 1
                    if cnt > max_cnt:
                        max_cnt = cnt
                else:
                    cnt = 0
    total_map = list(zip(*total_map))

    for i in range(m):
        cnt = 0
        if total_map[i].count(1) > max_size:
            for j in range(n):
                if total_map[i][j] == 1:
                    cnt += 1
                    if cnt > max_cnt:
                        max_cnt = cnt
                else:
                    cnt = 0
    print(f"#{tc+1} {max_cnt}")