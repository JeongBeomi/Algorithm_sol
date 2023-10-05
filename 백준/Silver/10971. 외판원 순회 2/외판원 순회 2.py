def dfs(start, now, visited, move_length):
    global answer
    # 만약 앞에서 구한 최소거리보다 길어지면 더이상 확인할 필요 x
    if move_length >= answer:
        return
    
    # 출발한 지점으로 돌아오고, 모든 도시를 방문 했다면 순회 성공
    if start == now and False not in visited:
        answer = move_length
    
    # 다음 도시로 이동
    for city in range(len(visited)):
        # 길이 존재하고, 방문한적 없어야 한다
        if cities[now][city] != 0 and not visited[city]:
            visited[city] = True
            dfs(start, city, visited, move_length + cities[now][city])
            visited[city] = False

n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]
answer = 1000000 * n
visited = [False] * n

for i in range(n):
    dfs(i, i, visited, 0)

print(answer)