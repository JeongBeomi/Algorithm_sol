def solution(data, col, row_begin, row_end):
    answer = 0
    sort_data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    s_i_list = []
    for i in range(row_begin, row_end + 1):
        temp = 0
        for num in sort_data[i - 1]:
            temp += num % i
        s_i_list.append(temp)
    
    for j in range(len(s_i_list)):
        answer ^= s_i_list[j]
    
    return answer