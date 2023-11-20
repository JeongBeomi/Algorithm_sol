from collections import deque

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)


def bfs():
    cnt = 0
    global answer
    while q:
        cnt += 1
        # 불 확장
        for _ in range(len(fire)):
            r, c = fire.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m and building[nr][nc] in [".", "@"]:
                    building[nr][nc] = "*"
                    fire.append((nr, nc))

        # 상근이 이동
        for _ in range(len(q)):
            r, c = q.popleft()
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if 0 <= nr < n and 0 <= nc < m:
                    if building[nr][nc] == ".":
                        building[nr][nc] = "@"
                        q.append((nr, nc))
                else:
                    answer = cnt
                    return


t = int(input())
for _ in range(t):
    m, n = map(int, input().split())
    answer = "IMPOSSIBLE"
    building = [list(input()) for _ in range(n)]
    fire = deque()
    q = deque()
    for i in range(n):
        for j in range(m):
            if building[i][j] == "*":
                fire.append((i, j))
            elif building[i][j] == "@":
                q.append((i, j))

    bfs()
    print(answer)
