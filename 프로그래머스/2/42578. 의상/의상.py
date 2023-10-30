def solution(clothes):
    answer = 0
    clothes_dict = dict()
    for v, k in clothes:
        if k in clothes_dict:
            clothes_dict[k] += 1
        else:
            clothes_dict[k] = 1
    
    temp = 1
    for v in clothes_dict.values():
        temp *= v + 1
    answer = temp - 1
    return answer