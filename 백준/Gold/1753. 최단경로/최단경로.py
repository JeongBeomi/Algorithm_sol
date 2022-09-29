from heapq import heappush, heappop


def dijkstra(s):
    distance[s] = 0
    heap = [(0, s)]

    while heap:
        min_d, min_n = heappop(heap)

        if distance[min_n] < min_d:
            continue

        for next_n, next_d in graph[min_n]:
            new_d = distance[min_n] + next_d
            if distance[next_n] > new_d:
                distance[next_n] = new_d
                heappush(heap, (new_d, next_n))


v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
INF = 99999999
distance = [INF] * (v + 1)
for _ in range(e):
    v1, v2, w = map(int, input().split())
    graph[v1].append((v2, w))

dijkstra(k)
for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
        continue
    print(distance[i])
