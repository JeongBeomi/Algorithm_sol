def solution(s):
    answer = []
    s_list = list(map(lambda x : set(map(int, x.split(","))), s[2: len(s) - 2].split("},{")))
    s_list.sort(key = lambda x : len(x))
    answer.append(*s_list[0])
    
    for i in range(1, len(s_list)):
        answer.append(*(s_list[i] - s_list[i - 1]))
    
    return answer