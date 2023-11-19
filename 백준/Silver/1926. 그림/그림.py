from collections import deque

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)


def bfs(r, c):
    board[r][c] = 0
    q = deque([(r, c)])
    result = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 1:
                q.append((nr, nc))
                board[nr][nc] = 0
                result += 1

    return result


n, m = map(int, input().split())
cnt, max_size = 0, 0
board = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            cnt += 1
            max_size = max(bfs(i, j), max_size)

print(cnt, max_size, sep="\n")
