def solution(s, skip, index):
    answer = ''
    s_list = list(map(ord, s))
    skip_set = set(map(ord, skip))
    rotation_set = set(range(97, 123)) - skip_set
    rotation_list = sorted(list(rotation_set))
    
    for ch_s in s_list:
        idx = rotation_list.index(ch_s)
        idx = (idx + index) % len(rotation_list)
        answer += chr(rotation_list[idx])

    return answer