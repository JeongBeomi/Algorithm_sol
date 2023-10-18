from collections import deque

# 올바른 괄호인지 확인
def check(u):
    result = False
    s = deque()
    for i in range(len(u)):
        if u[i] == ")":
            if not s:
                break
            elif s[-1] == "(":
                s.pop()
                continue    
        s.append(u[i])
    else:
        if not s:
            result = True
    
    return result

# 재귀
def recur(w):
    # 빈문자열이면 빈문자열 반환
    if not w:
        return ""
    
    w = deque(w)
    u, v = "", ""
    left_cnt, right_cnt = 0, 0
    
    # w를 u, v로 분리
    for _ in range(len(w)):
        temp = w.popleft()
        if temp == "(":
            left_cnt += 1
        else:
            right_cnt += 1
        u += temp
        if left_cnt == right_cnt:
            v = "".join(w)
            break
    # 3번 로직
    if check(u):
        return u + recur(v)
    # 4번 로직
    else:
        temp = "(" + recur(v) + ")"
        for c in u[1 : -1]:
            if c == "(":
                temp += ")"
            else:
                temp += "("
        return temp
        
        
def solution(p):
    answer = ''
    answer = recur(p)
    
    return answer
