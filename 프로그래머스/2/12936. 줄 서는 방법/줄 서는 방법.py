def solution(n, k):
    answer = []
    total_cnt = 1
    num_list = list(range(1, n + 1))
    for i in range(1, n + 1):
        total_cnt *= i    
    k = k - 1
    while len(answer) < n:
        total_cnt = total_cnt // len(num_list)
        answer.append(num_list.pop(k // total_cnt))
        k = k % total_cnt
        
    
    return answer
'''
0 1 2 3 4 5 / 6 7 8 9 10 11 / 12 13 14 15 16

1 2 3 4  ..... 0
1 2 4 3  ..... 1
1 3 2 4  ..... 2
1 3 4 2  ..... 3
1 4 2 3  ..... 4
1 4 3 2  ..... 5
'''
