from collections import Counter

def solution(topping):
    answer = 0
    # 개수 비교를 위해 형은 추가만하면되기때문에 set, 동생은 감소를 해야하기 때문에 딕셔너리로 생성
    older = set()
    younger = Counter(topping)
    # for t in topping:
    #     if t in younger:
    #         younger[t] += 1
    #     else:
    #         younger[t] = 1
    
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