def bfs(i, j):
    maze[i][j] = 1
    q = [(i, j)]
    while q:
        i, j = q.pop()
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if maze[ni][nj] != 1:   # 1로 둘러 쌓여 있기 때문에 범위 비교 안해도 됨
                if maze[ni][nj] == 3:
                    return 1
                maze[ni][nj] = 1    # visited 대신 지나온 길을 1로 막는다.
                q.append((ni, nj))
    return 0


di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

for _ in range(10):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    print(f"#{n} {bfs(1, 1)}")