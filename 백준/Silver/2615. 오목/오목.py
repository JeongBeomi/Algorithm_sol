from collections import deque

def bfs(s_r, s_c, v):
    global answer
    # 우상향, 우하향, 상하, 좌우 4가지 경우의 오목 확인
    for i in range(4):
        # 정해진 방향으로 bfs
        visited = [[0] * 19 for _ in range(19)]
        q = deque([(s_r, s_c)])
        cnt = 1
        visited[s_r][s_c] = 1
        temp = [(s_r + 1, s_c + 1)]
        while q:
            r, c = q.popleft()
            for dr, dc in dm[i]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 19 and 0 <= nc < 19 and omok[nr][nc] == v and not visited[nr][nc]:
                    cnt += 1
                    q.append((nr, nc))
                    visited[nr][nc] = 1
                    # 오목일 때 행렬이 가장빠른 좌표 출력을 위해 담아둔다
                    temp.append((nr + 1, nc + 1))
            # 6이상이 되면 오목 넘어감 더 이상 확인 불필요
            if cnt >= 6:
                break
        
        # 한 방향으로 bfs 끝났을 때 cnt가 5라면 오목
        if cnt == 5:
            answer[0] = v
            answer.append(sorted(temp, key = lambda x : (x[1], x[0]))[0])

omok = [list(map(int, input().split())) for _ in range(19)]
# 4가지 방향 우상향, 우하향, 상하, 좌우
dm = [[(-1, 1), (1, -1)], [(-1, -1), (1, 1)], [(-1, 0), (1, 0)], [(0, -1), (0, 1)]]
answer = [0]
for i in range(19):
    if answer[0] != 0:
        break
    for j in range(19):
        if answer[0] != 0:
            break
        # 돌이 놓여있으면 오목 확인
        if omok[i][j] != 0:
            bfs(i, j, omok[i][j])

print(answer[0])
if answer[0] != 0:
    print(*answer[1])