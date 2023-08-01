def solution(brown, yellow):
    answer = []
    for i in range(1, int(yellow ** (1/2)) + 1):
        if yellow % i == 0 and (i + 2) * (yellow // i + 2) == brown + yellow :
            answer = [yellow // i + 2, i + 2]
    return answer