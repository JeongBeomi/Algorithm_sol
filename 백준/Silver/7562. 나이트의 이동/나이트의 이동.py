from collections import deque

def bfs():
    result = 0
    while knight:
        r, c, t = knight.popleft()
        # 목표한 좌표면 출력
        if r == target[0] and c == target[1]:
            result = t
            return result
        # 8방향으로 BFS
        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                knight.append((nr, nc, t + 1))
                
    return result
    

dr = (-2, -1, -2, -1, 1, 2, 2, 1)
dc = (-1, -2, 1, 2, 2, 1, -1, -2)

t = int(input())
for _ in  range(t):
    n = int(input())
    visited = [[False] * n for _ in range(n)]
    r, c = map(int, input().split())
    knight = deque([(r, c, 0)])
    target = list(map(int, input().split()))
    print(bfs())        