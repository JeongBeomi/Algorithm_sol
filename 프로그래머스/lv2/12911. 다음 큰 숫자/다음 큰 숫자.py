def solution(n):
    answer = n + 1
    one_cnt = bin(n).count("1")
    while bin(answer).count("1") != one_cnt:
        answer += 1
    return answer