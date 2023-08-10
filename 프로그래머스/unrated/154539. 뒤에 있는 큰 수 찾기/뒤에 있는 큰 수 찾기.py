# def solution(numbers):
#     answer = []
#     n = len(numbers)
#     s = []
#     for i in range(n - 1, -1, -1):
#         while s:
#             # stack 최근 넣은 숫자가 현재 숫자보다 작거나 같을 경우
#             if numbers[i] >= s[-1]:
#                 s.pop()
#             # 현재 숫자보다 stack 숫자가 작을 경우 해당 값이 가장 가까운 큰수이므로 answer에 추가
#             # 다음 숫자 비교를 위해 스택에 현재 numbers 숫자도 추가해준다
#             else:
#                 answer.append(s[-1])
#                 s.append(numbers[i])
#                 break
#         # 스택을 다돌았는데 큰수가 없거나, 스택이 원래 없을 경우
#         else:
#             answer.append(-1)
#             s.append(numbers[i])
        
#     return answer[::-1]

def solution(numbers):
    stack = []
    result = [-1] * len(numbers)
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            result[stack.pop()] = numbers[i]

        stack.append(i)

    return result
