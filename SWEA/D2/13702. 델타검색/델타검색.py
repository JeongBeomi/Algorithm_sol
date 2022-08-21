def my_abs(a, b):
    if a >= b:
        return a - b
    else:
        return b - a


drow = [-1, 1, 0, 0]
dcol = [0, 0, -1, 1]

for tc in range(10):
    cnt = 0
    n = int(input())
    list_a = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(4):
                ni = i + drow[k]
                nj = j + dcol[k]
                if 0 <= ni < n and 0 <= nj < n:
                    cnt += my_abs(list_a[i][j], list_a[ni][nj])
    print(f"#{tc + 1} {cnt}")