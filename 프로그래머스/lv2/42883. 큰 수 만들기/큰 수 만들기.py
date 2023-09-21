from collections import deque

def solution(number, k):
    answer = ''
    number_list = deque(list(number))
    num_cnt = len(number_list) - k
    s = deque()
    cnt = 0
    
    while number_list and cnt < k:
        num = number_list.popleft()
        while s and s[-1] < num:
            s.pop()
            cnt += 1
            if cnt == k:
                break
        s.append(num)
    
    answer = "".join(s) + "".join(number_list)
    
    return answer[:num_cnt]