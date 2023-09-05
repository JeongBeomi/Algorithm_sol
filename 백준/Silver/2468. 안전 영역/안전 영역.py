from collections import deque

def bfs(w, v, i, j):
    v[i][j] = 1
    q = deque([(i, j)])

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not v[nr][nc] and area[nr][nc] > w:
                v[nr][nc] = 1
                q.append((nr, nc))

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]
answer = 0

# 수위를 1씩 올려가며 탐색
water = 0
while water <= 100:
    cnt = 0
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            # 수위에 잠기지 않고 방문한적 없으면 안전영역 탐색 시작
            if area[i][j] > water and not visited[i][j]:
                bfs(water, visited, i, j)
                cnt += 1

    # 다잠기면 더이상 확인  x
    if cnt == 0:
        break

    # 더 많은 안전영역이 나오면 갱신
    if answer < cnt:
        answer = cnt
    # 수위 증가
    water += 1


print(answer)