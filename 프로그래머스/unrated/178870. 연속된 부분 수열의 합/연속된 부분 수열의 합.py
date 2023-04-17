def solution(sequence, k):
    answer = []
    n = len(sequence)

    num_sum = 0
    idx = 0
    min_length = n

    for start in range(n):
        while num_sum < k and idx < n:
            num_sum += sequence[idx]
            idx += 1
        if num_sum == k and idx-1-start < min_length:
            answer = [start, idx-1]
            min_length = idx-1-start
        num_sum -= sequence[start]

    return answer
