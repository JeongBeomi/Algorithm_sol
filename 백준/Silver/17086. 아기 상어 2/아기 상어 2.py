from collections import deque

def bfs(shark_pos):
    visited = [[0] * m for _ in range(n)]
    q = deque()

    for i, j in shark_pos:
        q.append((i, j, 0))
        visited[i][j] = 1
    
    while q:
        r, c, cnt = q.popleft()
        for d in range(8):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and sea[nr][nc] != "s":
                visited[nr][nc] = 1
                sea[nr][nc] = cnt + 1
                q.append((nr, nc, cnt + 1))

dr = [0, 0, 1, -1, -1, -1, 1, 1]
dc = [1, -1, 0, 0, -1, 1, -1, 1]
n, m = map(int, input().split())
sea = [list(map(int, input().split())) for _ in range(n)]
sharks = []

for i in range(n):
    for j in range(m):
        if sea[i][j] == 1:
            sharks.append((i, j))
            sea[i][j] = "s"

bfs(sharks)

max_d = 0
for i in range(n):
    for j in range(m):
        if sea[i][j] != "s" and max_d < sea[i][j]:
            max_d = sea[i][j]

print(max_d)