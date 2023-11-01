from collections import deque

dh = (1, -1, 0, 0, 0, 0)
dr = (0, 0, 0, 0, 1, -1)
dc = (0, 0, -1, 1, 0, 0)

def find_start():
    for i in range(m):
        for j in range(n):
            for k in range(l):
                if building[i][j][k] == "S":
                    return (i, j, k, 0)

def bfs(start):
    result = "Trapped!"
    q = deque([start])
    while q:
        h, r, c, t = q.popleft()
        for i in range(6):
            nh, nr, nc = h + dh[i], r + dr[i], c + dc[i]
            if 0 <= nh < m and 0 <= nr < n and 0 <= nc < l:
                if building[nh][nr][nc] == ".":
                    building[nh][nr][nc] = "#"
                    q.append((nh, nr, nc, t + 1))
                elif building[nh][nr][nc] == "E":
                    result = f"Escaped in {t + 1} minute(s)."
                    return result
    return result
                    

while True:
    m, n, l = map(int, input().split())
    # 0, 0, 0 입력시 종료
    if m == 0 and n == 0 and l == 0:
        break
    # 3차원 배열 입력받기
    building = [[list(input()) for _ in range(n + 1)][: -1] for _ in range(m)]
    answer = bfs(find_start())
    print(answer)