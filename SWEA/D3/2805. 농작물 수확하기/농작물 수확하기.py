t = int(input())
for tc in range(t):
    n = int(input())
    total_map = [list(map(int, input())) for _ in range(n)]
    m = n // 2
    result = 0
    for i in range(n):
        for j in range(n):
            if abs(m - i) + abs(m - j) <= m:
                result += total_map[i][j]
    print(f"#{tc + 1} {result}")