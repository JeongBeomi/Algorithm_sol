t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    map_list = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            cnt = 0
            for k in range(m):
                for p in range(m):
                    cnt += map_list[i + k][j + p]
            if max_cnt < cnt:
                max_cnt = cnt

    print(f"#{tc + 1} {max_cnt}")