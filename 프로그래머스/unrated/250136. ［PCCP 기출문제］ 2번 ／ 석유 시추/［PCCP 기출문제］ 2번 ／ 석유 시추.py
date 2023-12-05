from collections import deque

def bfs(land, r, c, oil_cnt):
    dr = (0, 0, 1, -1)
    dc = (1, -1, 0, 0)
    n, m = len(land), len(land[0])
    # 석유량
    result = 1
    # bfs시 방문하는 c좌표의땅에서는 해당 석유를 발견할 수 있다  
    c_set = set([c])
    q = deque([(r, c)])
    # 방문처리대신 해당 땅의 석유값을 0으로 바꿈
    land[r][c] = 0
    
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and land[nr][nc] == 1:
                q.append((nr, nc))
                land[nr][nc] = 0
                result += 1
                c_set.add(nc)
    
    # bfs를 진행한 석유를 시추할 수 있는 땅 위치에 석유량 추가해주기
    for col in c_set:
        oil_cnt[col] += result
    

def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    # 각땅에서 뽑을 수 있는 석유 카운트를 위한 리스트
    oil_cnt = [0] * m
    
    for i in range(n):
        for j in range(m):
            # 석유를 만나면 bfs로 석유 찾기
            if land[i][j] == 1:
                bfs(land, i, j, oil_cnt)
    
    return max(oil_cnt)