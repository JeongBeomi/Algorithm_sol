def dfs(s, e, p):
    global max_v
    if max_v >= p:      # 가지치기
        return
    if s == e:
        max_v = p
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            dfs(s + 1, e, p * percent[s][i] * (10**-2))
            visited[i] = False


t = int(input())
for tc in range(t):
    n = int(input())
    visited = [False] * n
    max_v = 0
    percent = [list(map(int, input().split())) for _ in range(n)]
    dfs(0, n, 1)
    print(f"#{tc + 1} {max_v * 100:.6f}")