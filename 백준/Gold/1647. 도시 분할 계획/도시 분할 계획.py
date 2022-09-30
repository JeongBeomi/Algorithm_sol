from heapq import heappush, heappop


def prim(s):
    visited = [False] * (n + 1)
    heap = [(0, s)]
    result = []

    while heap:
        min_w, min_n = heappop(heap)
        if visited[min_n]:
            continue

        visited[min_n] = True
        result.append(min_w)
        for next_n, next_w in graph[min_n]:
            if not visited[next_n]:
                heappush(heap, (next_w, next_n))
    return sorted(result, reverse=True)[1:]


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))
print(sum(prim(1)))