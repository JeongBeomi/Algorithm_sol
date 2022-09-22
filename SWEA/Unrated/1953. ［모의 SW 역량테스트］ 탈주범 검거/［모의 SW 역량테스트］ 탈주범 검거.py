from collections import deque


def bfs(r, c):
    visited = [[False] * m for _ in range(n)]
    visited[r][c] = 1
    cnt = 1                 # 탈주범이 위치할 수 있는 장소의 개수
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        for i in t_type[t_map[r][c]]:
            nr, nc = r + dr[i], c + dc[i]
            # 인덱스 범위 안에 좌표가 존재하고, 길이 연결되어 있고, 방문한 적이 없으면 이동
            if 0 <= nr < n and 0 <= nc < m and (movable[i] in t_type[t_map[nr][nc]]) and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                if visited[nr][nc] > l:     # 주어진 시간을 넘어서면 반환
                    return cnt
                cnt += 1
                q.append((nr, nc))
    return cnt      

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 구조물 타입을 인덱스로 이동 가능한 방향 저장
t_type = [(), (0, 1, 2, 3), (0, 1), (2, 3), (0, 3), (1, 3), (1, 2), (0, 2)]
# 가는 길이 열려 있는가
movable = [1, 0, 3, 2]

t = int(input())
for tc in range(t):
    n, m, r, c, l = map(int, input().split())
    t_map = [list(map(int, input().split())) for _ in range(n)]

    print(f"#{tc + 1}", bfs(r, c))