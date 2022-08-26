def omok(r, c):
    for dir in range(4):
        cnt = 1
        x, y = r, c
        while True:
            nr, nc = x + dr[dir], y + dc[dir]
            if 0 <= nr < n and 0 <= nc < n and total_map[nr][nc] == "o":
                cnt += 1
                x, y = nr, nc
            else:
                break
            if cnt >= 5:
                return "YES"
    return "NO"


# 하 우 우하향 우상향
dr = [1, 0, 1, -1]
dc = [0, 1, 1, 1]

t = int(input())
for tc in range(t):
    n = int(input())
    total_map = [list(input()) for _ in range(n)]

    result = "NO"
    for i in range(n):
        for j in range(n):
            if total_map[i][j] == 'o':
                result = omok(i, j)
            if result == "YES":
                break
        if result == "YES":
            break

    print(f"#{tc + 1} {result}")