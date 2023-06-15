from collections import deque

def dfs(v):
    s = deque([v])
    dfs_visited[v] = True

    while s:
        v = s.pop()
        print(v)
        for next_v in sorted(graph[v]):
            if not dfs_visited[next_v]:
                dfs_visited[next_v] = True
                dfs(next_v)


def bfs(v):
    q = deque([v])
    bfs_visited[v] = True

    while q:
        v = q.popleft()
        print(v)
        for next_v in sorted(graph[v]):
            if not bfs_visited[next_v]:
                bfs_visited[next_v] = True
                q.append(next_v)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

dfs_visited = [False] * (n + 1)
bfs_visited = [False] * (n + 1)

dfs(v)
bfs(v)