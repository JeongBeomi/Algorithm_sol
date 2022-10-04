from collections import deque


def bfs(r, c):
    visited = [[0] * n for _ in range(n)]
    visited[r][c] = 1
    q = deque([(r, c)])
    cnt = farm[r][c]
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                if visited[nr][nc] > 1 + n // 2:
                    break
                cnt += farm[nr][nc]
                q.append((nr, nc))
    return cnt


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
t = int(input())
for tc in range(t):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    result = 0
    print(f'#{tc + 1} {bfs(n // 2, n // 2)}')