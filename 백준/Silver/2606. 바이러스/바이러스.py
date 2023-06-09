from collections import deque

def dfs(start):
    visted = [False] * (n + 1)
    s = deque([start])
    visted[start] = True
    result = 0

    while s:
        v = s.pop()
        for next_v in graph[v]:
            if not visted[next_v]:
                s.append(next_v)
                visted[next_v] = True
                result += 1
    
    return result

n = int(input())
graph = [[] for _ in range(n + 1)]
m = int(input())

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(dfs(1))
