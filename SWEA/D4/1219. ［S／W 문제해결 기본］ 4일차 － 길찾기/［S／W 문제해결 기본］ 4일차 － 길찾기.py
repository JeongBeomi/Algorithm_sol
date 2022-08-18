def dfs(v):
    visited[v] = True
    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)


for _ in range(10):
    t, e = map(int, input().split())
    node_list = list(map(int, input().split()))
    graph = [[] for _ in range(100)]

    for i in range(0, e * 2, 2):
        v1, v2 = node_list[i], node_list[i + 1]
        graph[v1].append(v2)

    visited = [False] * 100

    dfs(0)
    if visited[99]:
        print(f"#{t} 1")
    else:
        print(f"#{t} 0")