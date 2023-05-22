def solution(sequence, k):
    answer = []

    l = len(sequence)
    min_length = l
    now_idx = 0
    sum_num = 0
    
    for start in range(l):
        while sum_num < k and now_idx < l:
            sum_num += sequence[now_idx]
            now_idx += 1
        if sum_num == k and now_idx - start - 1 < min_length:
            answer = [start, now_idx - 1]
            min_length = now_idx - start - 1
        
        sum_num -= sequence[start]

    return answer
