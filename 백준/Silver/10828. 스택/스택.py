import sys
input=sys.stdin.readline
from collections import deque

n = int(input())
s = deque()
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        s.append(int(command[1]))
    elif command[0] == "pop":
        if s:
            print(s.pop())
            continue
        print(-1)
    elif command[0] == "size":
        print(len(s))
    elif command[0] == "empty":
        if s:
            print(0)
            continue
        print(1)
    elif command[0] == "top":
        if s:
            print(s[-1])
            continue
        print(-1)
