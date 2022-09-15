def solution(x):
    answer = True
    num = sum(map(int, list(str(x))))
    if x % num != 0:
        answer = False
    return answer

print(solution(11))