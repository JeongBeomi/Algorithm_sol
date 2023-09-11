from collections import deque

dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

n, m = map(int, input().split())
buckets = [list(map(int, input().split())) for _ in range(n)]
# 비바라기 시전 초기 비구름 위치
cloud = deque([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])
# 직전에 비구름 위치 기록을 위한 배열
visited = [[0] * n for _ in range(n)]

# 비구름 이동을 순차적으로 실행
for i in range(1, m + 1):
    d, cnt = map(int, input().split())
    # 각 구름 이동, 방문처리, 바구니 물의 양 추가
    for idx, cloud_pos in enumerate(cloud):
        nr, nc = cloud_pos[0] + dr[d] * cnt, cloud_pos[1] + dc[d] * cnt
        # 이동 좌표 인덱스 범위 내로 계산
        nr = nr % n if nr >= 0 else (n - (abs(nr) % n)) % n
        nc = nc % n if nc >= 0 else (n - (abs(nc) % n)) % n
        # 이후 물복사를 위해 이동한 좌표로 수정해놓기
        cloud[idx] = (nr, nc)
        # 비내린 순번으로 방문처리 후 비내리기
        visited[nr][nc] = i
        buckets[nr][nc] += 1

    # 비내렸던 곳 물복사버그 마법 시전
    while cloud:
        r, c = cloud.popleft()
        cnt = 0
        for d in [2, 4, 6, 8]:
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and buckets[nr][nc] > 0:
                cnt += 1
        buckets[r][c] += cnt

    # 다음 구름 생성
    for c_r in range(n):
        for c_c in range(n):
            if buckets[c_r][c_c] >= 2 and visited[c_r][c_c] != i:
                cloud.append((c_r, c_c))
                buckets[c_r][c_c] -= 2

# 이동이 모두 끝난후 바구니에 들어있는 물의 양 합 출력
answer = 0
for line in buckets:
    answer += sum(line)
print(answer)