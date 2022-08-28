# 델타 이동
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

w, h = map(int, input().split())
# 가장 자리 이동 가능하도록 전체 맵 만들기 0 = 벽, 1 = 통로
total_map = [[0] * (w + 1) for _ in range(h + 1)]
total_map[0] = [1] * (w + 1)
total_map[h] = [1] * (w + 1)
for i in range(1, h):
    total_map[i][0] = 1
    total_map[i][w] = 1
# 상점과 내위치 맵에 위치시키기
n = int(input())
for _ in range(n + 1):
    v1, v2 = map(int, input().split())
    if v1 == 1:
        v1 = 0
    elif v1 == 2:
        v1 = h
    elif v1 == 3:
        v1, v2 = v2, 0
    else:
        v1, v2 = v2, w
    total_map[v1][v2] = 2   # 2는 상점과 내 위치

# 거리 탐색 시작
store_length = []
cnt = 0
total_map[v1][v2] = 0
while len(store_length) < n:
    for j in range(4):
        nr, nc = v1 + dr[j], v2 + dc[j]
        if 0 <= nr <= h and 0 <= nc <= w and total_map[nr][nc] != 0:
            cnt += 1
            v1, v2 = nr, nc
            if total_map[v1][v2] == 2:
                store_length.append(cnt)
            total_map[v1][v2] = 0
result = 0
for length in store_length:
    if length > w + h:
        result += 2 * (w + h) - length
    else:
        result += length

print(result)