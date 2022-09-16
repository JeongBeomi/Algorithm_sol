from collections import deque

def bfs(v):
    visited = [False] * 101
    visited[v] = 1
    queue = deque([v])
    result = [(v, 1)]
    while queue:
        v = queue.popleft()
        for next_v in graph[v]:
            if not visited[next_v]:
                visited[next_v] = visited[v] + 1
                result.append((next_v, visited[next_v]))
                queue.append(next_v)
    result.sort(key=lambda x : (x[1],x[0]))
    return result[-1]


for tc in range(10):
    n, s = map(int, input().split())
    edges = list(map(int, input().split()))     # 간선 정보 받기
    graph = [[] for _ in range(101)]            

    for i in range(0, n, 2):                    # 주어진 간선 정보에따라 그래프 생성
        v1, v2 = edges[i], edges[i + 1]
        if v2 in set(graph[v1]):
            continue
        graph[v1].append(v2)

    print(f"#{tc + 1} {bfs(s)[0]}")