from collections import deque

n, k = map(int ,input().split())
q = deque(list(range(1, n + 1)))
cnt = 1
result = []

while q:
    if cnt == k:
        result.append(q.popleft()) 
        cnt = 1

    else:
        q.append(q.popleft())
        cnt += 1

print("<" + str(result)[1:-1] + ">")