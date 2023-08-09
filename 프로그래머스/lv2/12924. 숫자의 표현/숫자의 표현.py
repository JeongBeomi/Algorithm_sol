def solution(n):
    answer = 0
    # 시작점, 끝점, 지금까지 합
    start_n = 1
    end_n = 1
    sum_n = 1
    # 시작 숫자가 n을 넘어가면 더이상 확인할 필요 없음
    while start_n <= n:
        # 지금까지 합이 n 보다 작으면 연속되는 숫자 하나 더해주기 
        if sum_n < n:
            end_n += 1
            sum_n += end_n
        # 지금까지 합이 n 보다 크면 맨앞의 숫 빼주기
        elif sum_n > n:
            sum_n -= start_n
            start_n += 1
        # n과 같을때 경우의수 + 1
        else:
            answer += 1
            end_n += 1
            sum_n += end_n
        
    return answer