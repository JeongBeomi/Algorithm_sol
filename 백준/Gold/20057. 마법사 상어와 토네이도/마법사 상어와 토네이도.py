def tornado(r, c, d):
    global answer
    total_sand = 0
    for i, j, k in dsand[d]:
        sr, sc, move_sand = r + i, c + j, int(sands[r][c] * k)
        if 0 <= sr < n and 0 <= sc < n:
            sands[sr][sc] += move_sand
        else:
            answer += move_sand
        total_sand += move_sand
    
    sr, sc = r + dr[d], c + dc[d] 
    if 0 <= sr < n and 0 <= sc < n:
        sands[sr][sc] += (sands[r][c] - total_sand)
    else:
        answer += (sands[r][c] - total_sand)
    sands[r][c] = 0

dsand = {
    0 : [(0, -2, 0.05), (-1, -1, 0.1), (1, -1, 0.1), (-1, 0, 0.07), (1, 0, 0.07), (-2, 0, 0.02), (2, 0, 0.02), (-1, 1, 0.01), (1, 1, 0.01)], 
    1 : [(2, 0, 0.05), (1, 1, 0.1), (1, -1, 0.1), (0, 1, 0.07), (0, -1, 0.07), (0, 2, 0.02), (0, -2, 0.02), (-1, 1, 0.01), (-1, -1, 0.01)],
    2 : [(0, 2, 0.05), (-1, 1, 0.1), (1, 1, 0.1), (-1, 0, 0.07), (1, 0, 0.07), (-2, 0, 0.02), (2, 0, 0.02), (1, -1, 0.01), (-1, -1, 0.01)],
    3 : [(-2, 0, 0.05), (-1, 1, 0.1), (-1, -1, 0.1), (0, 1, 0.07), (0, -1, 0.07), (0, 2, 0.02), (0, -2, 0.02), (1, 1, 0.01), (1, -1, 0.01)]
}

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

n = int(input())
visited = [[False] * n for _ in range(n)]
sands = [list(map(int, input().split())) for _ in range(n)]
r, c, d = n // 2, n // 2, 0
visited[r][c] = True
answer = 0

# 종료는 항상 0, 0
while r != 0 or c != 0:
    nr, nc = r + dr[d], c + dc[d]
    # 좌표 이동
    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
        # 모래가 존재하면 모래 이동
        if sands[nr][nc] != 0:
            # 좌표범위 밖으로 나간 모래양 더해주기
            tornado(nr, nc, d)
        visited[nr][nc] = True
        r, c = nr, nc

    # 방향을 바꿔서 갈 수 잇으면 방향 바꿔주고 아니면 기존 방향 유지
    nd = (d + 1) % 4
    if not visited[r + dr[nd]][c + dc[nd]]:
        d = nd

print(answer)