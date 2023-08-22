def solution(X, Y):
    answer = ''

    # 작은 갯수로 추가해주기 
    for i in range(9, -1, -1):
        X = X.split(str(i))
        Y = Y.split(str(i))
        cnt = min(len(X), len(Y)) - 1
        X = "".join(X)
        Y = "".join(Y)
        answer += str(i) * cnt
        
    if not answer:
        answer = "-1"
    elif answer[0] == "0":
        answer = "0"
        
    return answer