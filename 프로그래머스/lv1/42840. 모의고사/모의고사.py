def solution(answers):
    reuslt = []
    forks = [(1, 2, 3, 4, 5), (2, 1, 2, 3, 2, 4, 2, 5), (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)]
    # 1, 2, 3 사람들이 맞춘 개수
    temp = [0, 0, 0]
    for i, fork in enumerate(forks):
        n = len(fork)
        cnt = 0
        for j, answer in enumerate(answers):
            if answer == fork[j % n]:
                cnt += 1
        temp[i] = cnt
    
    m_cnt = max(temp)
    for i in range(3):
        if temp[i] == m_cnt:
            reuslt.append(i + 1)
            
    return reuslt