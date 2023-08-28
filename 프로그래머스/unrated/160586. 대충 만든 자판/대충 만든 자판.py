def solution(keymap, targets):
    answer = []
    alpa_dict = dict()
    for key in keymap:
        for i, k in enumerate(key):
            if k not in alpa_dict:
                alpa_dict[k] = i + 1
            else:
                alpa_dict[k] = min(alpa_dict[k], i + 1)
    
    for target in targets:
        cnt = 0
        for t in target:
            if alpa_dict.get(t) == None:
                cnt = -1
                break
            cnt += alpa_dict.get(t)
        answer.append(cnt)
                
    return answer