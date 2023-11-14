from collections import deque

n = int(input())
answer = []
s = deque()
razers = [(i + 1, v) for i, v in enumerate(map(int, input().split()))]

for i in range(n):
    receive_tower = 0
    while s and s[-1][1] <= razers[i][1]:
        s.pop()
    else:
        if s:
            receive_tower = s[-1][0]
        s.append(razers[i])

    answer.append(receive_tower)

print(*answer)
