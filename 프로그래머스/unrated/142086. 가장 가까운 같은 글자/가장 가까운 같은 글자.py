def solution(s):
    answer = []
    # 딕셔너리에 알파벳 : 마지막으로 나온 인덱스를 key : value 저장
    alpa_dict = {}
    for i in range(len(s)):
        # 딕셔너리에서 현재 찾는 알파벳의 마지막으로 나온 인덱스를 찾는다
        first_idx = alpa_dict.get(s[i])
        # 처음 나온 알파벳이라면 딕셔너리에 존재하지 않기 때문에 None
        if first_idx == None:
            answer.append(-1)
        else:
            answer.append(i - first_idx)
        # 해당 알파벳이 가장 최근에 나온 인덱스로 업데이트해준다
        alpa_dict[s[i]] = i
    return answer