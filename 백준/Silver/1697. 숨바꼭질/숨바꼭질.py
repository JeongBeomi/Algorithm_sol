from collections import deque
dr = {
    0 : lambda x : x + 1,
    1 : lambda x : x - 1,
    2 : lambda x : x * 2
}
n, k = map(int, input().split())
pos = [0] * 100001
# 출발점 q에 넣기, 방문처리 1
q = deque([(n, 0)])
pos[n] = 1

while q:
    i, cnt = q.popleft()
    # 다음좌표가 도착점이면 출력후 탈출
    if i == k:
        print(cnt)
        break

    for d in range(3):
        n_i = dr[d](i)    
        if 0 <= n_i <= 100000 and not pos[n_i]:
            q.append((n_i, cnt + 1))
            pos[n_i] = 1