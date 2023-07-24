def solution(ingredient):
    answer = 0
    idx = 0
    post_idx = -1
    
    while idx < len(ingredient) - 3:
        if ingredient[idx : idx + 4] == [1, 2, 3, 1]:
            answer += 1
            # for _ in range(4):
            #     ingredient.pop(idx)
            del ingredient[idx:idx+4]
            if idx >= 3:
                idx -= 3
            else:
                idx = 0    
        else: 
            idx += 1
        
    return answer 
