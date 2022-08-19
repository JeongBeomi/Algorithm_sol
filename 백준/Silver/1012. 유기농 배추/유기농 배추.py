import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    total_map[x][y] = 0
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and total_map[nx][ny] == 1:
            dfs(nx, ny)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
t = int(input())
for tc in range(t):
    m, n, e = map(int,input().split())
    cnt = 0
    # 전체 맵 만들기
    total_map = [[0] * n for _ in range(m)]
    # 배추 심기
    for i in range(e):
        row, col = map(int, input().split())
        total_map[row][col] = 1

    for j in range(m):
        for k in range(n):
            if total_map[j][k] == 1:
                dfs(j, k)
                cnt += 1

    print(cnt)