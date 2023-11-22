from collections import deque

answer = []
n = int(input())
s = deque()
num_list = list(map(int, input().split()))

for i in range(n - 1, -1, -1):
    while s and s[-1] <= num_list[i]:
        s.pop()
    if s:
        answer.append(s[-1])
    else:
        answer.append(-1)
    s.append(num_list[i])
print(*answer[::-1])
