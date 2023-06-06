from collections import deque

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]
t = int(input())
for _ in range(t):
    n = int(input()) + 2
    pos_list = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n

    result = "sad"
    q = deque([pos_list[0]])
    visited[0] = True

    while q:
        x, y = q.popleft()
        for i in range(1, n):
            if not visited[i]:
                next_x, next_y = pos_list[i]
                if abs(next_x - x) + abs(next_y - y) <= 1000:
                    if i == n - 1:
                        q = deque()
                        result = "happy"
                        break
                    visited[i] = True
                    q.append([next_x, next_y])

    print(result)
