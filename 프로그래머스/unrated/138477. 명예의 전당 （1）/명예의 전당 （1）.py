from collections import deque

def solution(k, score):
#     num_list = deque(sorted(score[:k]))
#     answer = [num_list[0] for _ in range(k)]
#     # 일차 진행을 위한 반복문
#     for i in range(k, len(score)):
#         # 명예의 전당 순위 갱신
#         for j in range(0, k):
#             if score[i] < num_list[j]:
#                 num_list.insert(j, score[i])
#                 break
#         else:
#             num_list.append(score[i])
            
#         num_list.popleft()
#         answer.append(num_list[0])

    answer = []
    num_list = []
    for num in score:
        num_list.append(num)
        num_list.sort()
        if len(num_list) > k:
            num_list.pop(0)
        
        answer.append(num_list[0])
            
    return answer