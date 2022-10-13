def solution(participant, completion):
    answer = ''
    runner = dict()
    for com in completion:
        if com not in runner:
            runner[com] = 1
        else:
            runner[com] += 1

    for part in participant:
        if part not in runner:
            answer = part
            break
        else:
            if runner[part] > 1:
                runner[part] -= 1
            else:
                del runner[part]
    return answer