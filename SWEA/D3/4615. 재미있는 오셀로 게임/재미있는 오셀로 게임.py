def reverse_d(r, c, p):
    for dir in range(8):
        flag = False
        temp = []
        t_r, t_c = r, c
        while True:
            nr = t_r + dr[dir]
            nc = t_c + dc[dir]
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == r_dol[p]:
                temp.append((nr, nc))   # 반전시킬 돌 좌표 넣어두기
                t_r, t_c = nr, nc           # 좌표 이동
                flag = True             # 반전 진행 여부

            # 좌표범위안 and 반전진행중 and 시작점과 색이 같은 돌이면 반전
            elif 0 <= nr < n and 0 <= nc < n and flag and board[nr][nc] == p:
                for x, y in temp:
                    board[x][y] = p  # 돌 반전
                    cnt[p] += 1             # 반전된 만큼 카운트 갱신
                    cnt[r_dol[p]] -= 1
                break
            else:
                break
    return


# 상하좌우 대각선
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]
# 다른색 돌 찾기  1 -> 2/ 2 -> 1
r_dol = [0, 2, 1, 0]

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]     # 보드 초기화
    board[n // 2 - 1][n // 2], board[n // 2 ][n // 2 - 1] = 1, 1
    board[n // 2 - 1][n // 2 - 1], board[n // 2][n // 2] = 2, 2
    cnt = [0, 2, 2]     # 흑돌 수, 백돌 수
    for i in range(m):
        col, row, dol = map(int, input().split())
        row, col = row - 1, col - 1     # 인덱스에 맞게 변환
        cnt[dol] += 1                   # 주어진 돌 놓기
        board[row][col] = dol
        reverse_d(row, col, dol)        # 색 반전 확인

    print(f"#{tc + 1}", *cnt[1:])