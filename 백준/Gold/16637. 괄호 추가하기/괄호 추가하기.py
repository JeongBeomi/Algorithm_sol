from collections import deque


def dfs(p, state):
    global max_v
    if p == n:
        stack = deque(line)
        result = deque([])
        idx = 0
        while stack:    # 괄호 처리
            s = stack.popleft()
            if idx in gwal:
                result.append(cal[s](result.pop(), stack.popleft()))
                idx += 1
            else:
                result.append(s)
            idx += 1
        answer = result.popleft()
        while result:
            m = result.popleft()
            y = result.popleft()
            answer = cal[m](answer, y)

        if max_v < answer:
            max_v = answer
        return

    if state:
        gwal.append(p)
        dfs(p + 2, 0)
        gwal.pop()
        dfs(p + 2, 1)
    else:
        dfs(p + 2, 1)


cal = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
}
n = int(input())
# line = list(input())
line = [int(i) if i.isnumeric() else i for i in input()]
max_v = (-2) ** 31
gwal = deque([])
dfs(1, 1)   # 연산자 위치, 해당연산자 괄호칠 수 있는가
print(max_v)