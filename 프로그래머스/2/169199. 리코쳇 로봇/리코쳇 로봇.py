from collections import deque

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)

def move(board, r, c, d):
    n, m = len(board), len(board[0])
    nr, nc = r + dr[d], c + dc[d]
    while 0 <= nr < n and 0 <= nc < m and board[nr][nc] == ".":
        r, c = nr, nc
        nr, nc = r + dr[d], c + dc[d]
    return (r, c)

def bfs(board, visited):
    result = -1
    n, m = len(board), len(board[0])
    q = deque()
    tr, tc = 0, 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == "R":
                q.append((i, j, 0))
                board[i][j] = "."
            elif board[i][j] == "G":
                tr, tc = i, j
                board[i][j] = "."
                
    while q:
        r, c, t = q.popleft()
        for d in range(4):
            nr, nc = move(board, r, c, d)
            if not visited[nr][nc]:
                visited[nr][nc] = 1
                if nr == tr and nc == tc:
                    result = t + 1
                    return result
                else:
                    q.append((nr, nc, t + 1))
    return result
    
def solution(board):
    answer = 0
    for i in range(len(board)):
        board[i] = list(board[i])
    # 각 위치에서 4개의 방향에 대한 방문처리 리스트
    visited = [[0] * len(board[0]) for _ in range(len(board))]
    answer = bfs(board, visited)
    return answer