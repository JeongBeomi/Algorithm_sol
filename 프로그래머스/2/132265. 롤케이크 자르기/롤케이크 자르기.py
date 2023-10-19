def solution(topping):
    answer = 0
    older = set()
    younger = dict()
    for t in topping:
        if t in younger:
            younger[t] += 1
        else:
            younger[t] = 1
    
    for t in topping:
        older.add(t)
        younger[t] -= 1
        if younger[t] == 0:
            del younger[t]
        if len(younger) == len(older):
            answer += 1
        elif len(younger) < len(older):
            break
    
    return answer