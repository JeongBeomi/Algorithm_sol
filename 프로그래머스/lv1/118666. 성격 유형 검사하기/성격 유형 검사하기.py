def solution(survey, choices):
    answer = ''
    q_types = ("R", "T", "C", "F", "J", "M", "A", "N")
    score_dict = {k : 0 for k in q_types}
    # 1 2 3 4 5 6 7 -> 3 2 1 0 1 2 3
    scores = (0, 3, 2, 1, 0, 1, 2, 3)
    for i in range(len(choices)):
        if choices[i] == 4:
            continue
        # 1->0 0->1 점수를 부여할 성격 유형 인덱스 찾아서 점수부여
        type_idx = choices[i] // 4
        score_dict[survey[i][type_idx]] += scores[choices[i]]
    # 점수가 높은 유형으로 문자열 만들기
    for i in range(0, len(q_types), 2):
        if score_dict[q_types[i]] >= score_dict[q_types[i + 1]]:
            answer += q_types[i]
        else:
            answer += q_types[i + 1]

    return answer