def solution(name, yearning, photo):
    answer = []
    score_dict = {name[i] : yearning[i] for i in range(len(name))}
    for p in photo:
        total_score = 0
        for n in p:
            if score_dict.get(n) == None:
                continue
            total_score += score_dict.get(n)
        answer.append(total_score)
    return answer