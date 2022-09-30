from heapq import heappush, heappop

def prim(s):
    visited = [False] * n
    heap = [(0, s)]
    cost = 0

    while heap:
        min_d, min_n = heappop(heap)
        if visited[min_n]:
            continue

        visited[min_n] = True
        cost += e * min_d

        for i in range(n):
            if not visited[i]:
                dist = abs(x[min_n] - x[i]) ** 2 + abs(y[min_n] - y[i]) ** 2
                heappush(heap, (dist, i))
    return cost


t = int(input())
for tc in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())
    print(f"#{tc + 1} {round(prim(0))}")

