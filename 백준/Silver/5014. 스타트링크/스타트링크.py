from collections import deque

f, s, g, u, d = map(int, input().split())

answer = "use the stairs"
floors = [0] * (f + 1)

q = deque([s])
floors[s] = 1
while q:
    now_f = q.popleft()
    for i in (u, -d):
        next_f = now_f + i
        if 1 <= next_f <= f and not floors[next_f]:
            floors[next_f] = floors[now_f] + 1
            q.append(next_f)
    
    if floors[g] != 0:
        answer = floors[g] - 1
        break

print(answer)    