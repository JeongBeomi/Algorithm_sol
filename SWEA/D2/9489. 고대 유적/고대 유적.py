t = int(input())
for tc in range(t):
    n, m  = map(int, input().split())
    total_map = [list(map(int, input().split())) for _ in range(n)]

    max_cnt = 0
    for i in range(n):
        cnt = 0
        for j in range(m):
            if total_map[i][j]:
                cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
            else:
                cnt = 0

    for i in range(m):
        cnt = 0
        for j in range(n):
            if total_map[j][i]:
                cnt += 1
                if max_cnt < cnt:
                    max_cnt = cnt
            else:
                cnt = 0
    print(f"#{tc + 1} {max_cnt}")