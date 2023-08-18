import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    visited = [0] * (n + 1)
    q = deque([s])
    visited[s] = 1
    cnt = 1

    while q:
        v = q.popleft()
        for n_v in graph[v]:
            if not visited[n_v]:
                cnt += 1
                q.append(n_v)
                visited[n_v] = 1
    return cnt

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

for start in range(1, n + 1):
    answer.append((start, bfs(start)))

answer.sort(key = lambda x : (-x[1], x[0]))

for i, c in answer:
    if c < answer[0][1]:
        break
    print(i, end=" ")