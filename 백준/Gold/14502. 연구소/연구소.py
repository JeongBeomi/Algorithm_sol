from collections import deque
# 벽세우기
def wall(s, r_l, c_l, c):
    global min_v
    # 벽을 3개 세웠다면 bfs
    if c == 3:
        result = bfs()
        # 결과 값의 바이러스가 수가 더적으면 갱신
        if min_v > result:
            min_v = result
        return
    # 순서대로 모든 경우의 수에 대해서 벽 세워보기
    for i in range(s, r_l * c_l):
        if laboratory[i // c_l][i % c_l] == 0:
            laboratory[i // c_l][i % c_l] = 1
            wall(i + 1, r_l, c_l, c + 1)
            laboratory[i // c_l][i % c_l] = 0

# 바이러스 bfs
def bfs():
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for i, j in start_points:
        visited[i][j] = True
    q = deque(start_points)
    
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and laboratory[nr][nc] == 0:
                visited[nr][nc] = True
                q.append((nr, nc))
                cnt += 1
                # 지금까지 바이러스 최소값 보다 커지면 더이상 확인할 필요 x     
                if cnt >= min_v:
                    return cnt
    return cnt

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

n, m = map(int, input().split())
start_points = []
laboratory = [list(map(int, input().split())) for _ in range(n)]
z_cnt = 0
min_v = n * m
# 바이러스 시작점 찾기
for i in range(n):
    for j in range(m):
        if laboratory[i][j] == 2:
            start_points.append((i, j))
        elif laboratory[i][j] == 0:
            z_cnt += 1

# 벽세우기 및 bfs
wall(0, n, m, 0)

print(z_cnt - 3 - min_v)