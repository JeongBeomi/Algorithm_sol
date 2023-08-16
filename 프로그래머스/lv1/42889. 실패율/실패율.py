def solution(N, stages):
    answer = []
    # 해당인덱스의 스테이지를 클리어한 인원수
    clear_num = [0 for _ in range(N + 1)]
    # stages 리스트를 순회하며 클리어 인원수 세기
    for s in stages:
        for i in range(0, s):
            clear_num[i] += 1
    temp = []
    # 1 ~ N 까지 스테이지의 실패율 계산
    for j in range(1, N + 1):
        # 실패율 계산
        p = 0
        if clear_num[j - 1] != 0:
            p = 1 - clear_num[j] / clear_num[j - 1]
        # (인덱스, 실패율) 실패율은 1 - (현재스테이지 클리어수) / (이전 스테이지 클리어수)
        temp.append((j, p))
    
    # 정렬 후 answer에 스테이지만 순서대로 넣어주기
    temp.sort(key = lambda x : (-x[1], x[0]))
    for i in range(N):
        answer.append(temp[i][0])
        
    return answer