def dfs(idx, cnt, nocnt):
    global min_v, no_connect
    if nocnt > no_connect:
        return

    if idx == ea:
        if nocnt < no_connect:
            min_v = cnt
        else:
            if min_v > cnt:
                min_v = cnt
        no_connect = nocnt
        return

    for d in range(4):
        c = 1
        connectable = False
        while True:
            row = chk_p[idx][0] + dr[d] * c
            col = chk_p[idx][1] + dc[d] * c
            if not (1 <= row < n - 1 and 1 <= col < n - 1) and matrix[row][col] == 0:
                connectable = True
                break
            elif matrix[row][col] == 1:
                break
            c += 1
        if connectable:
            for i in range(c):
                nr = row - dr[d] * i
                nc = col - dc[d] * i
                matrix[nr][nc] = 1
            dfs(idx + 1, cnt + c, nocnt)
            for i in range(c):
                nr = row - dr[d] * i
                nc = col - dc[d] * i
                matrix[nr][nc] = 0
        else:
            dfs(idx + 1, cnt, nocnt + 1)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
t = int(input())
for tc in range(t):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    chk_p = []
    min_v = n * n
    no_connect = n * n
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if matrix[i][j] == 1:
                chk_p.append((i, j))
    ea = len(chk_p)
    dfs(0, 0, 0)   # core순서, 전선길이, 연결불가칩의 수
    print(f"#{tc + 1} {min_v}")