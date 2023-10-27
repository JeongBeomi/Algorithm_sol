from collections import deque

def check_tomatos():
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomatos[i][j][k] == 0:
                    return -1
    return answer 

# 위,아래,상,하,좌,우
d_pos = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))

answer = 0
m, n, h = map(int, input().split())
visited = [[[0] * m for _ in range(n)] for _ in range(h)]
q = deque()
# 토마토 3차원 배열을 만들면서 익은 토마토를 q에 담는다
tomatos = []
for i in range(h):
    temp = []
    for j in range(n):
        line = list(map(int, input().split()))
        temp.append(line)
        for k, t in enumerate(line):
            if t == 1:
                q.append((i, j, k, 0))
    tomatos.append(temp)

# BFS
while q:
    u, r, c, d = q.popleft()
    for i in range(6):
        nu, nr, nc = u + d_pos[i][0], r + d_pos[i][1], c + d_pos[i][2]
        if 0 <= nu < h and 0 <= nr < n and 0 <= nc < m and tomatos[nu][nr][nc] == 0:
            tomatos[nu][nr][nc] = 1
            q.append((nu, nr, nc, d + 1))
            if d + 1 > answer:
                answer = d + 1

print(check_tomatos())