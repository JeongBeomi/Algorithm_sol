from collections import deque


def bfs(ball_drop):
    global block_cnt
    # co_matrix = deepcopy(matrix)
    co_matrix = [line[:] for line in matrix]
    for col in ball_drop:
        row = 0
        for i in range(h):  # 구슬이 처음만나는 벽돌 찾기.
            if co_matrix[i][col] != 0:
                row = i
                break
        else:   # 처음만나는 벽돌을 찾지못하면 다음 공으로 넘어가기.
            continue
        # 연쇄폭발 시작
        q = deque([(row, col)])
        while q:
            r, c = q.popleft()
            temp = co_matrix[r][c]
            co_matrix[r][c] = 0
            for j in range(1, temp):
                for d in range(4):
                    nr = r + dr[d] * j
                    nc = c + dc[d] * j
                    if 0 <= nr < h and 0 <= nc < w and co_matrix[nr][nc] != 0:
                        q.append((nr, nc))
        # 벽돌 내리기
        for i in range(w):
            for j in range(h - 1, -1, -1):
                if co_matrix[j][i] == 0:
                    for k in range(j - 1, -1, -1):
                        if co_matrix[k][i] != 0:
                            co_matrix[j][i], co_matrix[k][i] = co_matrix[k][i], co_matrix[j][i]
                            break
                    else:
                        break

    # 끝나면 블럭 개수 확인
    cnt = 0
    for i in range(h):
        cnt += w - co_matrix[i].count(0)
    if cnt < block_cnt:
        block_cnt = cnt


def dfs(s, ball_drop):
    if s == n:
        bfs(ball_drop)
        return
    for i in range(w):
        ball_drop.append(i)
        dfs(s + 1, ball_drop)
        ball_drop.pop()


# 하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
t = int(input())
for tc in range(t):
    n, w, h = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(h)]
    block_cnt = w * h
    dfs(0, [])
    print(f"#{tc + 1} {block_cnt}")