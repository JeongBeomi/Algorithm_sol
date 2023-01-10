from collections import deque

def solution(queue1, queue2):
    answer = -1
    queue1, queue2 = deque(queue1), deque(queue2)
    q1_sum, q2_sum = sum(queue1), sum(queue2)
    end = len(queue1) * 3
    i = 0
    while i <= end:
        if q1_sum > q2_sum:
            temp = queue1.popleft()
            queue2.append(temp)
            q1_sum -= temp
            q2_sum += temp
        elif q1_sum < q2_sum:
            temp = queue2.popleft()
            queue1.append(temp)
            q2_sum -= temp
            q1_sum += temp
        else:
            answer = i
            break
        i += 1
        

    return answer