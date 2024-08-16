import heapq

dr = (0, 0, 1, -1)
dc = (1, -1, 0, 0)
idx = 0

while True:
    idx += 1
    n = int(input())
    if n == 0:
        break

    cave = [list(map(int, input().split())) for _ in range(n)]
    distance = [[n * n * 10] * n for _ in range(n)]
    hq = [(cave[0][0], 0, 0)]
    distance[0][0] = cave[0][0]

    while hq:
        min_d, r, c = heapq.heappop(hq)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and distance[nr][nc] > min_d + cave[nr][nc]:
                distance[nr][nc] = min_d + cave[nr][nc]
                heapq.heappush(hq, (distance[nr][nc], nr, nc))

    print("Problem {}: {}".format(idx, distance[n - 1][n - 1]))
