def solution(order):
    answer = 0
    subcontain = []
    box = 1
    while box <= len(order):
        # 일단 스택으로 보내서 비교하면 조건 분기가 간단해짐
        subcontain.append(box)
        while subcontain and subcontain[-1] == order[answer]:
            answer += 1
            subcontain.pop()
        box += 1

    return answer
