def solution(msg):
    answer = []
    az = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lwz_dict = {v : i + 1 for i, v in enumerate(az)}
    num = 27
    i = 0
    while i < len(msg):
        s = msg[i]
        while i < len(msg) - 1:
            i += 1
            s += msg[i]
            # 다음 글자를 합친 문자열이 딕셔너리에 없으면 새로운 색인 추가
            if s not in lwz_dict:
                answer.append(lwz_dict[s[:-1]])
                lwz_dict[s] = num
                num += 1
                break
        else:
            answer.append(lwz_dict[s])
            break
    return answer
