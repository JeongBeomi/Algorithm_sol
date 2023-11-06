from itertools import permutations
from collections import deque

cacul_dict = {
    "*" : lambda x, y : x * y,
    "+" : lambda x, y : x + y,
    "-" : lambda x, y : x - y
}

def cacul(per, e):
    e = deque(e)
    for p in per:
        cnt = 0
        n = len(e)
        while cnt < n:
            temp = e.popleft()
            if temp == p:
                cnt += 1
                e.append(cacul_dict[temp](e.pop(), e.popleft()))
            else:
                e.append(temp)
            cnt += 1
    return abs(e[0])
    
def solution(expression):
    answer = 0
    expression_list = []
    temp = ""
    for e in expression:
        if e in ("*", "+", "-"):
            expression_list.append(int(temp))
            expression_list.append(e)
            temp = ""
            continue
        temp += e
    else:
        expression_list.append(int(temp))

    for per in permutations(["*", "+", "-"], 3):
        answer = max(answer, cacul(per, expression_list))
    
    return answer