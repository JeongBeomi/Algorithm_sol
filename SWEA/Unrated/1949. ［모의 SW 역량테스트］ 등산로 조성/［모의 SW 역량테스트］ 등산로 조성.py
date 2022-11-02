def dfs(r, c, m, dis):
    global max_value
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and matrix[nr][nc] - m < matrix[r][c]:
            temp = matrix[nr][nc]
            visited[nr][nc] = 1
            if matrix[nr][nc] >= matrix[r][c]:
                dig = 1 + matrix[nr][nc] - matrix[r][c]
                matrix[nr][nc] -= dig
                dfs(nr, nc, 0, dis + 1)
                matrix[nr][nc] = temp
            else:
                dfs(nr, nc, m, dis + 1)
            visited[nr][nc] = 0
        else:
            if dis > max_value:
                max_value = dis


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    start = 0
    max_value = 0

    for i in range(n):
        if start < max(matrix[i]):
            start = max(matrix[i])

    for i in range(n):
        for j in range(n):
            if start == matrix[i][j]:
                visited = [[0] * n for _ in range(n)]
                visited[i][j] = 1
                dfs(i, j, k, 0)
    print(f"#{tc + 1} {max_value + 1}")