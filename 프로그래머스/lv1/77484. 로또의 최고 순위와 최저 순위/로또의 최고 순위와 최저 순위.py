def solution(lottos, win_nums):
    answer = []
    win_nums = set(win_nums)
    result = 6 - len(win_nums - set(lottos))
    for i in [result + lottos.count(0), result]:
        if i >= 2:
            answer.append(7-i)
        else:
            answer.append(6)
    return answer
