def dfs(v):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


t = int(input())
for tc in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    for i in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [False] * (n + 1)
    cnt = 0
    for j in range(1, n + 1):
        if not visited[j]:
            cnt += 1
            dfs(j)
    print(f"#{tc+1} {cnt}")