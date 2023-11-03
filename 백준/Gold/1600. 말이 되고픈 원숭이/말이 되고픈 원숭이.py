from collections import deque

def bfs():
    result = -1
    # 말이동으로 왔을때, 원숭이 이동으로 왔을때 각각 방문처리
    visited = [[set() for _ in range(w)] for _ in range(h)]
    # r, c, 이동 동작수, 말 점프 사용회숫
    q = deque([(0, 0, 0, 0)])
    while q:
        r, c, t, skill = q.popleft()
        s, e = (0, 12) if skill < k else (8, 12)
        for i in range(s, e):
            nr, nc = r + dr[i], c + dc[i]
            temp = skill + 1 if 0 <= i < 8 else skill
            if nr == h - 1 and nc == w - 1:
                result = t + 1
                return result
            elif 0 <= nr < h and 0 <= nc < w and travel[nr][nc] == 0:
                if temp not in visited[nr][nc]:
                    visited[nr][nc].add(temp)
                    q.append((nr, nc, t + 1, temp))

    return result

# 0 ~ 7 말 움직임, 8 ~ 11 원숭이 움직임
dr = (-1, -2, -2, -1, 1, 2, 2, 1, 0, 0, 1, -1)
dc = (-2, -1, 1, 2, 2, 1, -1, -2, 1, -1, 0, 0)

k = int(input())
w, h = map(int, input().split())
travel = [list(map(int, input().split())) for _ in range(h)]

if w == 1 and h == 1:
    print(0)
else:
    print(bfs())