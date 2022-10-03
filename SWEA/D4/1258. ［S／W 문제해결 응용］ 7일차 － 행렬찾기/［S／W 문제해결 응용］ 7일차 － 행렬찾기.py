def f(r, c):
    sr = r
    sc = c
    row = 1
    col = 1
    while True:     # row
        r += 1
        if r < n and arr[r][c] != 0 and visit[r][c] == False:
            row += 1
        else:
            r -= 1
            break
    while True:     # col
        c += 1
        if c < n and arr[r][c] and not visit[r][c]:
            col += 1
        else:
            c -= 1
            break

    for idx in range(sr, r+1):
        for jdx in range(sc, c+1):
            visit[idx][jdx] = True

    return [row, col]


t = int(input())

for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visit = [[False] * n for _ in range(n)]
    result = []
    for i in range(n):
        for j in range(n):
            # 0이 아닌 값 & 방문하지 않은 지점이면 돌면서 행렬 크기를 측정한다.
            if arr[i][j] and not visit[i][j]:
                result.append(f(i, j))
    # 행렬의 크기를 첫 번재, 같은 사이즈라면 행의 크기를 기준으로 정렬
    result = sorted(result, key=lambda x: (x[0]*x[1], x[0]))
    print(f'#{tc + 1} {len(result)}', end=' ')
    for line in result:
        print(*line, end=' ')
