from collections import deque

def bfs(p):
    global t_cnt
    visited = [[0] * n for _ in range(n)]
    visited[p[0]][p[1]] = 1
    q = deque([(p[0], p[1])])
    fish = []
    length = 400
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and matrix[nr][nc] <= shark[0]:
                if length < visited[r][c]:
                    continue
                if 1 <= matrix[nr][nc] < shark[0]:
                    fish.append((nr, nc, visited[r][c]))
                    length = visited[r][c]
                else:
                    q.append((nr, nc))

                visited[nr][nc] = visited[r][c] + 1
    return fish


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
now_pos = []
t_cnt = 0
for i in range(n):
    if now_pos:
        break
    for j in range(n):
        if matrix[i][j] == 9:
            now_pos = [i, j]
            break

shark = [2, 0]  # 현재 크기, 먹은 고기 수
while True:
    fishes = bfs(now_pos)
    if not fishes:
        break
    fishes.sort(key=lambda x: (x[0], x[1]))
    i, j, t = fishes[0]
    matrix[now_pos[0]][now_pos[1]] = 0
    matrix[i][j] = 0
    now_pos = [i, j]
    t_cnt += t
    shark[1] += 1
    if shark[0] == shark[1]:
        shark = [shark[0] + 1, 0]

print(t_cnt)

