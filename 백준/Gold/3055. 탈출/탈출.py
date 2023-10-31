from collections import deque

def move(q, water):
    global answer
    # 물 확장
    for _ in range(len(water)):
        r, c = water.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and forest[nr][nc] in (".", "S"):
                forest[nr][nc] = "*"
                water.append((nr, nc))

    # 고슴도치 이동
    for _ in range(len(q)):
        r, c, t = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m:
                if forest[nr][nc] == ".":
                    forest[nr][nc] = "S"
                    q.append((nr, nc, t + 1))
                elif forest[nr][nc] == "D":
                    answer = t + 1
                    return
    return

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

answer = "KAKTUS"
n, m = map(int, input().split())
forest = [list(input()) for _ in range(n)]
water = deque()
q = deque()

# 고슴도치 위치 및 물 위치 찾기
for i in range(n):
    for j in range(m):
        if forest[i][j] == "S":
            q.append((i, j, 0))
        elif forest[i][j] == "*":
            water.append((i, j))
    
# BFS
while q and answer == "KAKTUS":
    move(q, water)
    
print(answer)