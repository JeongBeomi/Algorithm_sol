from collections import deque

n = int(input())
q = deque()
answer = []
for idx, num in enumerate(map(int, input().split())):
    q.append((num, idx + 1))

while q:
    n, i = q.popleft()
    answer.append(i)
    
    if not q:
        break

    if n > 0:
        for _ in range(abs(n) - 1):
            q.append(q.popleft())
    else:
        for _ in range(abs(n)):
            q.appendleft(q.pop())

print(*answer)
