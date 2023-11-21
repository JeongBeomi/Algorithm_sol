from collections import deque

def solution(n, t, m, p):
    answer = ''
    num = 0
    num_type = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F")
    n_num = []
    while len(n_num) <= (t - 1) * m + p:
        temp = deque()
        temp_num = num
        while temp_num >= n:
            temp.appendleft(temp_num % n)
            temp_num = temp_num // n
        else:
            temp.appendleft(temp_num)
            
        n_num.extend(temp)
        num += 1
        
    for i in range(0, t):
        answer += num_type[n_num[i * m + p - 1]]
    return answer