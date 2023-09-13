from collections import deque

def wall(wall_cnt, start):
    if wall_cnt == 3:
        result = sol()
        return result
    
    for i in range(start, n * n):
        if corridor[i // n][i % n] == "X":
            corridor[i // n][i % n] = "O"
            result = wall(wall_cnt + 1, i + 1)
            # True 반환시 감시 피하는 경우를 찾은것 리턴으로 종료
            if result:
                return result
            corridor[i // n][i % n] = "X"

def sol():
    global answer
    # 상하좌우 중 한뱡향 정해서 이동시키며 확인
    for d in range(4):
        q = deque(start_pos)
        while q:
            r, c = q.popleft()
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n:
                if corridor[nr][nc] == "X":
                    q.append((nr, nc))
                # 학생과 만나면 감시 피할수 없다
                elif corridor[nr][nc] == "S":
                    return False
    # BFS가 다돌았다면 학생을 만난적 없음 -> 감시 피하기 성공
    answer = "YES"
    return True
        
dr = (0, 0, -1, 1)
dc = (-1, 1, 0, 0)
n = int(input())
corridor = [input().split() for _ in range(n)]
start_pos = []
answer = "NO"
# 선생님들 위치 찾기
for i in range(n):
    for j in range(n):
        if corridor[i][j] == "T":
            start_pos.append((i, j))

wall(0, 0)
print(answer)