def solution(order):
    answer = 0
    subcontain = []
    box = 1
    while box <= len(order):
        subcontain.append(box)
        while subcontain and subcontain[-1] == order[answer]:
            answer += 1
            subcontain.pop()
        box += 1

    return answer


print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))
