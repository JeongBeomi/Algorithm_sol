def dfs(r, c, n):
    arr[n] = str(board[r][c])
    if n == 6:
        if "".join(arr) not in result:
            result.add("".join(arr))
        return
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, n + 1)


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
t = int(input())
arr = [0] * 7
for tc in range(t):
    result = set()
    board = [list(map(int, input().split())) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            dfs(i, j, 0)
    print(f"#{tc + 1} {len(result)}")
