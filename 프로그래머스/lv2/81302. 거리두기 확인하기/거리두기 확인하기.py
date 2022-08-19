def solution(places):
    answer = []
    for i in range(5):
        for j in range(5):
            if len(answer) == i + 1:
                break
            for k in range(5):
                if len(answer) == i + 1:
                    break
                if places[i][j][k] == "P":
                    # 상하좌우 탐색
                    for n in range(4):
                        # 상하좌우 한칸 차이 탐색
                        nj, nk = j + drow[n], k + dcol[n]
                        if 0 <= nj < 5 and 0 <= nk < 5 and places[i][nj][nk] == "P":
                            answer.append(0)
                            break
                        # 상하좌우 두칸 차이인경우 탐색
                        nj2, nk2 = nj + drow[n], nk + dcol[n]
                        if 0 <= nj2 < 5 and 0 <= nk2 < 5 and places[i][nj2][nk2] == "P":
                            if not places[i][nj][nk] == "X":
                                answer.append(0)
                                break
                    # 상하좌우 이상 없다면 대각선 탐색
                    if len(answer) == i + 1:
                        break
                    for m in range(4, 8):
                        nj3, nk3 = j + drow[m], k + dcol[m]
                        if 0 <= nj3 < 5 and 0 <= nk3 < 5 and places[i][nj3][nk3] == "P":
                            # 파티션 있을 때만 거리두기 성공
                            if places[i][nj3][k] == "X" and places[i][j][nk3] == "X":
                                pass
                            else:
                                answer.append(0)
                                break
        else:
            if len(answer) == i + 1:
                continue
            answer.append(1)
    return answer


drow = [-1, 1, 0, 0, -1, -1, 1, 1]
dcol = [0, 0, -1, 1, -1, 1, 1, -1]
