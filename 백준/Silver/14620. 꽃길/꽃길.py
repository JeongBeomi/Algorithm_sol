def planting(r, c):
    money = 0
    visited[r][c] = not visited[r][c]
    money += land[r][c]

    # 꽃이 피는 좌표 가격 더하기 및 방문처리
    for dr, dc in flower:
        nr, nc = r + dr, c + dc
        visited[nr][nc] = not visited[nr][nc]
        money += land[nr][nc]
    
    return money

# 심을수 있는지 확인
def checking(r, c):
    for dr, dc in flower:
        nr, nc = r + dr, c + dc
        if visited[nr][nc]:
            return False
    return True         


def dfs(m, cnt):
    global min_value

    if cnt == 3:
        min_value = min(min_value, m)
        return

    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if checking(i, j):
                dfs(m + planting(i, j), cnt + 1)
                # 다음 재귀를 위해 꽃심기전으로 되돌리기
                planting(i, j)

# 꽃이 피는 좌표 이동
flower = [(0, 1), (0, -1), (1, 0), (-1, 0)]

n = int(input())
land = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
min_value = 3000

dfs(0, 0)
        
print(min_value)