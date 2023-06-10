from collections import deque

t = int(input())

for _ in range(t):
    vps = input()
    s = deque()
    result = "NO"
    for c in vps:
        if c == "(":
            s.append(c)
        elif c == ")":
            if not s:
                print(result)
                break
            else:
                s.pop()
    else:
        if not s:
            result = "YES"
        
        print(result)