from collections import deque

def solution(s):
    answer = 0
    n = len(s)
    
    pair_dict = {
        "}" : "{",
        ")" : "(",
        "]" : "["
    }
    # x만큼 회전시킬 때 시작 인덱스 
    for x in range(n):
        temp = deque()
        # 올바른 괄호 문자열인지 확인
        for i in range(x, x + n):
            if s[i % n] in {"{", "(", "["}:
                temp.append(s[i % n])
            else:
                # 닫히는 괄호가 나왔을 때 스택 temp가 비어있거나 짝이 아니면 올바르지 않음
                if not temp or temp[-1] != pair_dict[s[i % n]]:
                    break
                temp.pop()
        else:
            if not temp:
                answer += 1
            
    return answer