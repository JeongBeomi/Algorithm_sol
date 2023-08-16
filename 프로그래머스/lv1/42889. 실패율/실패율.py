def solution(N, stages):
    answer = []
    stage_user = len(stages)
    # 1 ~ N 까지 스테이지의 실패율 계산
    temp = []
    for j in range(1, N + 1):
        # 실패율 계산
        fail_p = 0
        if stage_user != 0:
            cnt = stages.count(j)
            fail_p = cnt / stage_user
            stage_user -= cnt
        temp.append((j, fail_p))

    # 정렬 후 answer에 스테이지만 순서대로 넣어주기
    temp.sort(key = lambda x : (-x[1], x[0]))
    for i in range(N):
        answer.append(temp[i][0])
        
    return answer



