from collections import deque
def solution(priorities, location):
    answer = 0
    q = deque([(idx, v) for idx, v in enumerate(priorities)])
    while q:
        idx, priority = q.popleft()
        for i in range(len(q)):
            if q[i][1] > priority:
                q.append((idx, priority))
                break
        else:
            answer += 1
            if idx == location:
                break
                
    return answer

