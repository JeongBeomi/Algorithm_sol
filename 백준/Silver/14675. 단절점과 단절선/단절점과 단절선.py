import sys
input = sys.stdin.readline
n = int(input())
# 간선 입력이 부모 자식 정확하지 않음 -> 양방향 그래프로 생각해야한다
t_graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    t_graph[a].append(b)
    t_graph[b].append(a)

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    # 노드제거는 무조건 단절선, 한 정점 두개이상의 정점 연결되어있으면 단절점
    if t == 2 or len(t_graph[k]) >= 2:
        print("yes")
        continue
    print("no")