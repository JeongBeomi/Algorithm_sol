def solution(babbling):
    answer = 0
    able_set = {"aya", "ye", "woo", "ma"}
    for word in babbling:
        visited = ""
        while word:
            if word[:3] in able_set and word[:3] != visited:
                visited = word[:3]
                word = word[3:]
            elif word[:2] in able_set and word[:2] != visited:
                visited = word[:2] 
                word = word[2:]
            else:
                break
                
        else: 
            answer += 1
    
    return answer