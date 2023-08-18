def solution(n, m, section):
    answer = 1
    # 시작 지점
    start_pos = section.pop(0)
    
    for s in section:
        # 시작점부터 색칠한 칸범위보다 크면 새로운곳에서 칠하기 시작
        if start_pos + m - 1 < s:
            answer += 1
            start_pos = s
    return answer