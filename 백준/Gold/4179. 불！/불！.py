from collections import deque
dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

def bfs():
    global answer

    # 불 확장
    for _ in range(len(fire)):
        r, c = fire.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] in (".", "J"):
                fire.append((nr, nc))
                maze[nr][nc] = "F"
                

    # 지훈 이동
    for _ in range(len(jihun)):
        r, c, t = jihun.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if maze[nr][nc] == ".":
                    jihun.append((nr, nc, t + 1))
                    maze[nr][nc] = "J"
            else:
                answer = t + 1
                return


answer = "IMPOSSIBLE"
n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)]
jihun = deque()
fire = deque()
# 불과 지훈이 위치 찾기
for i in range(n):
    for j in range(m):
        if maze[i][j] == "J":
            jihun.append((i, j, 0))
        elif maze[i][j] == "F":
            fire.append((i, j))

while jihun and answer == "IMPOSSIBLE":
    bfs()

print(answer)