def bingo(num):
    cnt = 0
    breaker = False
    # 사회자가 부른 번호 빙고판에서 찾아서 0처리
    for i in range(5):
        for j in range(5):
            if bingo_map[i][j] == num:
                bingo_map[i][j] = 0
                breaker = True
                break
        if breaker:
            break
    sum1, sum2 = 0, 0
    # 빙고 탐색
    re_map = list(zip(*bingo_map))      # 세로 탐색을 위한 뒤집기

    for i in range(5):
        if sum(bingo_map[i]) == 0:      # 가로 탐색
            cnt += 1
        if sum(re_map[i]) == 0:         # 세로 탐색
            cnt += 1

        for j in range(5):              # 대각선 탐색
            if i == j:
                sum1 += bingo_map[i][j]
            if i + j == 4:
                sum2 += bingo_map[i][j]
    if sum1 == 0:
        cnt += 1
    if sum2 == 0:
        cnt += 1

    if cnt >= 3:
        return True
    else:
        return False


bingo_map = [list(map(int, input().split())) for _ in range(5)]
call_num = []

# 사회자가 부르는 번호는 1차원 리스트로 저장
for _ in range(5):
    for num in map(int, input().split()):
        call_num.append(num)

cnt = 0
for i in range(25):
    if bingo(call_num[i]):
        print(i + 1)
        break