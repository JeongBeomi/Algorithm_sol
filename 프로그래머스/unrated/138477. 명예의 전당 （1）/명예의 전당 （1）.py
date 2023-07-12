from collections import deque

def solution(k, score):
    answer = []
    num_list = []
    for num in score:
        num_list.append(num)
        num_list.sort()
        if len(num_list) > k:
            num_list.pop(0)
        
        answer.append(num_list[0])
            
    return answer