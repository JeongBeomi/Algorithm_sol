from collections import deque

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]
    # 양방향 그래프
    for wire in wires:
        v1, v2 = wire
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    # 하나의 엣지가 끊어져있다면 두개의 정점중 하나의 정점의 자식정점 개수를 구해본다.
    for wire in wires:
        v1, v2 = wire
        visited = [False] * (n + 1)
        visited[v1], visited[v2] = True, True
        q = deque([v1])
        cnt = 1
        while q:
            v = q.popleft()
            for nv in graph[v]:
                if not visited[nv]:
                    cnt += 1
                    q.append(nv)
                    visited[nv] = True
                    
        # 두 정점의 자식정점수 차이가 적으면 업데이트
        if abs(n - 2 * cnt) < answer:
            answer = abs(n - 2 * cnt)
    
    return answer