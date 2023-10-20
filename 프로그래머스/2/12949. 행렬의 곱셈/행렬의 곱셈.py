def solution(arr1, arr2):
    answer = []
    for a1 in arr1:
        temp = []
        for a2 in zip(*arr2):
            sum_num = 0
            for i in range(len(a1)):
                sum_num += a1[i] * a2[i]
            temp.append(sum_num)
        answer.append(temp)
    
    return answer
