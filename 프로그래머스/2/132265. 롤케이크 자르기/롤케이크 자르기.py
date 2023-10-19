def solution(topping):
    answer = 0
    # 개수 비교를 위해 형은 추가만하면되기때문에 set, 동생은 감소를 해야하기 때문에 딕셔너리로 생성
    older = set()
    younger = dict()
    for t in topping:
        if t in younger:
            younger[t] += 1
        else:
            younger[t] = 1
    
    # 토핑을 하나씩 형쪽으로 넘기면서 개수가 동일할 때 answer += 1
    for t in topping:
        older.add(t)
        younger[t] -= 1
        # 토핑이 0이되면 삭제
        if younger[t] == 0:
            del younger[t]
        # 토핑 개수 비교
        if len(younger) == len(older):
            answer += 1
        # 형이 더 커지면 그때부터는 같아질 수 없다
        elif len(younger) < len(older):
            break
    
    return answer