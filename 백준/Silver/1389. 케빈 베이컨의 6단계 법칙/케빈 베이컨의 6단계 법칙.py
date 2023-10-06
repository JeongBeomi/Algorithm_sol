from collections import deque

def bfs(num):
    global answer
    total_cnt = 0
    visited = [False] * (n + 1)
    q = deque([(num, 0)])
    visited[num] = True

    while q:
        v, cnt = q.popleft()
        for nv in graph[v]:
            if not visited[nv]:
                q.append((nv, cnt + 1))
                total_cnt += cnt + 1
                visited[nv] = True
    
    if answer[0] > total_cnt:
        answer = [total_cnt, num]

n, m = map(int, input().split())
answer = [n * n, 0]
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(1, n + 1):
    bfs(i)

print(answer[1])