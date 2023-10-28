def solution(str1, str2):
    answer = 0
    str1_dict, str2_dict = dict(), dict()
    for i in range(0, len(str1) - 1):
        w = str1[i : i + 2]
        if w.isalpha():
            if w.upper() in str1_dict:
                str1_dict[w.upper()] += 1
            else:
                str1_dict[w.upper()] = 1
    for i in range(0, len(str2) - 1):
        w = str2[i : i + 2]
        if w.isalpha():
            if w.upper() in str2_dict:
                str2_dict[w.upper()] += 1
            else:
                str2_dict[w.upper()] = 1
            
    str1_set = set(str1_dict.keys())
    str2_set = set(str2_dict.keys())
    
    intersection_cnt = 0
    union_cnt = 0
    for w in str1_set & str2_set:
        intersection_cnt += min(str1_dict[w], str2_dict[w])
    for w in str1_set | str2_set:
        union_cnt += max(str1_dict[w] if w in str1_dict else 0, str2_dict[w] if w in str2_dict else 0)
    
    jaccard = 1
    if union_cnt != 0:
        jaccard = intersection_cnt / union_cnt
    answer = int(jaccard * 65536)
    return answer
