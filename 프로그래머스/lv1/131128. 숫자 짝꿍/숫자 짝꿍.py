def solution(X, Y):
    answer = ''
    
    for i in range(9, -1, -1):
        cnt = min(X.count(str(i)), Y.count(str(i)))
        answer += str(i) * cnt
    
    if not answer:
        answer = "-1"
    elif answer[0] == "0":
        answer = "0"
        
    return answer