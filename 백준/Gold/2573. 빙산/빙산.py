from collections import deque

def count_ice():
    result = 0
    visited = set()
    # 각 빙산에서 BFS 진행
    for k in ice_dict.keys():
        # 방문하지 않은 빙산이면 BFS 실행
        if k not in visited:
            # BFS
            result += 1
            q = deque([k])
            visited.add(k)
            while q:
                r, c = q.popleft()
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if (nr, nc) in ice_dict and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))
    
    return result




dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

answer = 0
n, m = map(int, input().split())
# 빙산 좌표 key, 빙산 크기 value
ice_dict = dict()
for i in range(n):
    for j, v in enumerate(map(int, input().split())):
        if v != 0:
            ice_dict[(i, j)] = v

after_year = 0
while ice_dict:
    after_year += 1
    # 녹는 빙산 찾기
    melt_ice = []
    for k, v in ice_dict.items():
        r, c = k
        # 주위 물 개수 구하기
        water_cnt = 0
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            # 주위 좌표가 얼음 목록에 없으면 물
            if (nr, nc) not in ice_dict:
                water_cnt += 1
        # 빙산녹는 정도를 리스트에 저장해 둔다
        if water_cnt > 0:
            melt_ice.append((r, c, water_cnt))
    
    # 빙산 녹이기
    for r, c, water_cnt in melt_ice:
        if ice_dict[(r, c)] - water_cnt <= 0:
            del(ice_dict[(r, c)])
        else:
            ice_dict[(r, c)] -= water_cnt

    # 빙산 덩어리 카운트
    ice_cnt = count_ice()
    if ice_cnt >= 2:
        answer = after_year
        break

print(answer)