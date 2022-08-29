di1 = [0, 1, 0, -1]
dj1 = [1, 0, -1, 0]
di2 = [1, 1, -1, -1]
dj2 = [1, -1, -1, 1]

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_result = 0
    for i in range(n):
        for j in range(n):
            cnt = arr[i][j]
            # 상하좌우 방향
            for k in range(4):
                for p in range(1, m):
                    ni, nj = i + di1[k] * p, j + dj1[k] * p
                    if 0 <= ni < n and 0 <= nj < n:
                        cnt += arr[ni][nj]
            if max_result < cnt:
                max_result = cnt
            
            cnt = arr[i][j]
            for k in range(4):
                for p in range(1, m):
                    ni, nj = i + di2[k] * p, j + dj2[k] * p
                    if 0 <= ni < n and 0 <= nj < n:
                        cnt += arr[ni][nj]

            if max_result < cnt:
                max_result = cnt

    print(f"#{tc + 1} {max_result}")