# 북동남서
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)

n, m = map(int, input().split())
r, c, d = map(int ,input().split())
room = [list(map(int, input().split())) for _ in range(n)]
answer = 0

while 0 <= r < n and 0 <= c < m :
    # 현재위치 청소
    if room[r][c] == 0:
        answer += 1
        room[r][c] = 2
    # 현재칸 주변 4칸 청소 상태 확인, 90도 회전을 먼저하기 때문에 1부터 시작
    for i in range(-1, -5, -1):
        nd = (d + i) % 4
        nr, nc = r + dr[nd], c + dc[nd]
        # 청소안한칸이 있으면 해당 칸으로 이동
        if 0 <= nr < n and 0 <= nc < m and room[nr][nc] == 0:
            r, c, d = nr, nc, nd
            break
    # 주위 4칸 청소되지 않은 칸이 없을때
    else:
        # 현재방향 유지한 상태로 뒤로 후진
        nd = (d + 2) % 4
        nr, nc = r + dr[nd], c + dc[nd]
        # 벽이면 종료
        if room[nr][nc] == 1:
            break
        # 이동가능하면 이동
        r, c = nr, nc
    
print(answer)