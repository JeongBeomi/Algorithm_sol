t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(n)]
    max_cnt = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            cnt = 0
            for row in range(m):
                for col in range(m):
                    cnt += total_map[i + row][j + col]

            if max_cnt < cnt:
                max_cnt = cnt

    print(f"#{tc + 1} {max_cnt}")