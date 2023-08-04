from collections import deque
def solution(maps):
    answer = -1
    n, m = len(maps), len(maps[0])
    dr = (-1, 1, 0, 0)
    dc = (0, 0, -1, 1)
    # 시작점 방문처리 및 큐
    maps[0][0] = 0
    q = deque([(0, 0, 1)])
    while q:
        r, c, d = q.popleft()
        # 도착했는지 확인
        if [r, c] == [n - 1, m - 1]:
            answer = d
            break
            
        # 좌표이동
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc]:
                q.append((nr, nc, d + 1))
                maps[nr][nc] = 0
    print(maps)
    return answer