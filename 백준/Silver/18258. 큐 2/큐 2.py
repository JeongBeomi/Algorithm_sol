from collections import deque
import sys

n = int(sys.stdin.readline())

q = deque()

for _ in range(n):
    command_list = sys.stdin.readline().split()

    if command_list[0] == "push":
        q.append(command_list[1])
    elif command_list[0] == "pop":
        if not q:
            print(-1)
            continue
        print(q.popleft())
    elif command_list[0] == "size":
        print(len(q))
    elif command_list[0] == "empty":
        if not q:
            print(1)
            continue
        print(0)
    elif command_list[0] == "front":
        if not q:
            print(-1)
            continue
        print(q[0])
    elif command_list[0] == "back":
        if not q:
            print(-1)
            continue
        print(q[-1])