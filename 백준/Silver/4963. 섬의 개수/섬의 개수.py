import sys
sys.setrecursionlimit(10000)


def dfs(row, col):
    total_map[row][col] = 0
    for i in range(8):
        nrow, ncol = row + drow[i], col + dcol[i]
        if 0 <= nrow < h and 0 <= ncol < w and total_map[nrow][ncol] == 1:
            dfs(nrow, ncol)


# 상 하 좌 우 대각선
drow = [-1, 1, 0, 0, -1, -1, 1, 1]
dcol = [0, 0, -1, 1, -1, 1, 1, -1]

while True:
    w, h = map(int, input().split())
    # 0 0 입력시 탈출
    if w == 0 and h == 0:
        break
    # 지도 생성
    total_map = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if total_map[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)