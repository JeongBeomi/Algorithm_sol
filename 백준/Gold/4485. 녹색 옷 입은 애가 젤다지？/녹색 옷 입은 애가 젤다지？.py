
import heapq

dr = (0, 0, -1, 1)
dc = (1, -1, 0, 0)

num = 1
while True:
    n = int(input())
    if n == 0:
        break

    cave = []
    for _ in range(n):
        cave.append(list(map(int, input().split())))

    distance = [[n * n * 9] * n for _ in range(n)]
    hq = [(cave[0][0], 0, 0)]
    distance[0][0] = cave[0][0]

    while hq:
        min_dist, r, c = heapq.heappop(hq)
        if min_dist > distance[r][c]:
            continue
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if (
                0 <= nr < n
                and 0 <= nc < n
                and distance[nr][nc] > min_dist + cave[nr][nc]
            ):
                distance[nr][nc] = cave[nr][nc] + min_dist
                heapq.heappush(hq, (distance[nr][nc], nr, nc))

    print("Problem {}: {}".format(num, distance[n - 1][n - 1]))
    num += 1