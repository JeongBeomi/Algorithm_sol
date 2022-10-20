def solution(answers):
    answer = []
    fork = [(1, 2, 3, 4, 5), (2, 1, 2, 3, 2, 4, 2, 5), (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)]
    temp = []
    for i in range(3):
        cnt = 0
        for j in range(len(answers)):
            if answers[j] == fork[i][j % len(fork[i])]:
                cnt += 1
        temp.append((cnt, i + 1))
    temp.sort(key=lambda x: (-x[0], x[1]))

    for k in range(len(temp)):
        cnt, idx = temp[k]
        if not answer or temp[k - 1][0] == cnt:
            answer.append(idx)
        else:
            break
    return answer

