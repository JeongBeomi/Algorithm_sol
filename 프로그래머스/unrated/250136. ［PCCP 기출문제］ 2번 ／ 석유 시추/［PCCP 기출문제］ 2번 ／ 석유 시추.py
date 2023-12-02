from collections import deque

def bfs(land, r, c, v):
    dr = (0, 0, 1, -1)
    dc = (1, -1, 0, 0)
    n, m = len(land), len(land[0])
    q = deque([(r, c)])
    land[r][c] = v
    cnt = 1
    
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < m and land[nr][nc] == 1:
                land[nr][nc] = v
                cnt += 1
                q.append((nr, nc))
    
    return cnt
    
def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    # 이미 찾은 석유의 양 기록을 위한 딕셔너리
    oil_dict = dict()
    
    # 시추 지점
    for c in range(m):
        temp = 0
        visited_set = set()
        # 해당 지점에 존재하는 석유 찾기
        for r in range(n):
            # 석유 존재 지점
            if land[r][c] != 0:
                # 처음 발견 -> bfs
                if land[r][c] == 1:
                    # 석유 카운트
                    oil_cnt = bfs(land, r, c, str(len(oil_dict)))
                    # 딕셔너리 업데이트 이때 키값은 딕셔너리 길이 -> land에도 방문표시로 딕셔너리 길이 문자값 넣을 예정
                    oil_dict[str(len(oil_dict))] = oil_cnt
                    temp += oil_cnt
                # 찾은적 있으니까 oil_dict에서 값 확인
                elif land[r][c] not in visited_set:
                    temp += oil_dict[land[r][c]]
                
                # 방문처리
                visited_set.add(land[r][c])
        
        answer = max(answer, temp)
                    
    return answer