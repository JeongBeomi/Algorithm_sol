def solution(N, stages):
    answer = []
    stage_probability = []
    # 스테이지 마다 실패율 구하기
    for i in range(1, N + 1):
        count = 0
        user = 0
        for stage in stages:
            if i <= stage:
                user += 1
                if i == stage:
                    count += 1
        if user == 0:
            probability = 0
        else:
            probability = count / user
        stage_probability.append((probability, i))

    for m in sorted(stage_probability, key=lambda x: -x[0]):
        answer.append(m[1])
    return answer


print(solution(4, [4, 4, 4, 4, 4]))
