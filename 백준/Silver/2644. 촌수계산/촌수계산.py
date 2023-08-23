from collections import deque

n = int(input())
s, e = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n + 1)]
answer = -1

# 그래프 입력받기
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

# BFS
visited = [False] * (n + 1) 
q = deque([(s, 0)])

while q:
    v, cnt = q.popleft()
    if v == e:
        answer = cnt
        break
    for n_v in graph[v]:
        if not visited[n_v]:
            q.append((n_v, cnt + 1))
            visited[n_v] = True

print(answer)