from collections import deque

text = input()
trigger = input()
n, m = len(text), len(trigger)
s = deque()
answer = "FRULA"

for i in range(n):
    if text[i] == trigger[-1] and len(s) >= m - 1:
        for j in range(2, m + 1):
            if s[-j + 1] != trigger[-j]:
                break
        else:
            for _ in range(m - 1):
                s.pop()
            continue
    s.append(text[i])

if s:
    answer = "".join(s)

print(answer)
