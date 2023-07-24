from collections import deque
def solution(s):
    answer = True
    stack = deque()
    
    for ch in s:
        if ch == "(":
            stack.append(ch)
        elif not stack:
            answer = False
            break
        else:
            stack.pop()
    else:
        if stack:
            answer = False
    
    return answer