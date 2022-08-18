def dfs(v):
    visited[v] = True         # 시작 정점 방문 처리

    for next_v in graph[v]:
        if not visited[next_v]: # 방문하지 않은 다음 인접 정점 탐색
            global cnt
            cnt += 1            # 감염 컴퓨터 증가
            dfs(next_v)         # 다음 인접 정점으로 이동


# 정점 개수, 간선 개수
n = int(input())
m = int(input())

# 그래프를 인접 리스트로 만들기 / 1~7을 인덱스 0~6으로 처리해서 -1
graph = [[] for _ in range(n)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1-1].append(v2-1)
    graph[v2-1].append(v1-1)

# 그래프를 인접행렬로 만들기
# graph = [[0] * n for _ in range(n)]
# for _ in range(m):
#     v1, v2 = map(int, input().split())
#     graph[v1-1][v2-1] = 1
#     graph[v2-1][v1-1] = 1

visited = [False] * n   # 방문 처리 초기화
cnt = 0

dfs(0)      # 정점 1~7을 인덱스 0~6으로 정했기 때문에 함수 맨처음 값을 1-1=0을 넣음
print(cnt)  # 정점을 0~7로 8개 만들어서 0은 간선이 없는 것으로 처리하는게 편할듯.