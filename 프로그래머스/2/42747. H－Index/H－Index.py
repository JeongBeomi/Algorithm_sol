def solution(citations):
    answer = 0
    citations.sort(reverse = True)
    # 개수가 i + 1 개일때 citations[i]가 i + 1보다 커야 한다
    for i in range(len(citations)):
        if citations[i] >= i + 1:
            answer += 1
        else:
            break
    return answer