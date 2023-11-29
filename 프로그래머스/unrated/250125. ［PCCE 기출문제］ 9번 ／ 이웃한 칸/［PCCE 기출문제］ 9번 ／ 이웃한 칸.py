from collections import deque

dr = [0, 1, -1, 0]
dc = [1, 0, 0, -1]

def solution(board, h, w):
    answer = 0
    n = len(board)
    visited = [[0] * n for _ in range(n)]
    color = board[h][w]
    q = deque([(h, w)])
    visited[h][w] = 1
    
    # while q:
    r, c = q.popleft()
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and board[nr][nc] == color:
            answer += 1
            visited[nr][nc] = 1
            q.append((nr, nc))
                
    return answer