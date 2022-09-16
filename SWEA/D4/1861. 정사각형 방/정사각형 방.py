def d_search(r, c):
    cnt = 1
    while True:
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < n and 0 <= nc < n and room[nr][nc] - room[r][c] == 1:
                r, c = nr, nc
                cnt += 1
                break
        else:
            return cnt


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

t = int(input())
for tc in range(t):
    n = int(input())
    room = [list(map(int, input().split())) for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):                              # 시작하는 방좌표          
            result.append((room[i][j], d_search(i, j))) # (시작 방번호, 갈 수 있는 방의 수)
    result.sort(key=lambda x : (x[1], -x[0]), reverse=True)
    print(f"#{tc + 1}", *result[0])
