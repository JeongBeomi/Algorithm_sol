def solution(n):
    answer = ''
    num_list = ["1", "2", "4"]
    
    while n != 0:
        n, m = n // 3, n % 3
        if m == 0:
            n -= 1
            answer = num_list[-1] + answer
        else:
            answer = num_list[m - 1] + answer
    
    return answer