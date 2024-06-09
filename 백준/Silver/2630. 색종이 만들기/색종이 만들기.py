def check_color(r, c, n):
    color = paper[r][c]

    for i in range(r, r + n):
        for j in range(c, c + n):
            if paper[i][j] != color:
                check_color(r, c, n // 2)
                check_color(r, c + n // 2, n // 2)
                check_color(r + n // 2, c, n // 2)
                check_color(r + n // 2, c + n // 2, n // 2)
                return

    cnt[color] += 1


n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
cnt = [0, 0]

check_color(0, 0, n)

for c in cnt:
    print(c)
