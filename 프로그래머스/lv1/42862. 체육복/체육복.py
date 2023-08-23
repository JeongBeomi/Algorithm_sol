def solution(n, lost, reserve):
    answer = 0
    lost = set(lost)
    # 여분있지만 도난당한 사람 먼저 구해서 빼기
    temp = set(lost) & set(reserve)
    lost -= temp
    reserve = sorted(list(set(reserve) - temp))
    
    for r in reserve:
        if r - 1 in lost:
            lost -= {r - 1}
        elif r + 1 in lost:
            lost -= {r + 1}
    
    answer = n - len(lost)
    return answer