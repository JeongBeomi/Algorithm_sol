mining_energy = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
mineral_to_pos = {"diamond": 0, "iron": 1, "stone": 2}


def mining(picks, minerals, idx, e):
    if picks == [0, 0, 0] or len(minerals) == idx:
        return e

    result = []
    for i in range(3):
        # 해당 곡괭이가 존자할 한다면 사용
        if picks[i] > 0:
            temp_e = 0
            # 남은 미네랄이 5개 이하인 경우 생각
            for j in range(min(5, len(minerals) - idx)):
                temp_e += mining_energy[i][mineral_to_pos[minerals[idx + j]]]
            # 다음 작업으로 넘어간다
            picks[i] -= 1
            result.append(
                mining(picks, minerals, idx + min(5, len(minerals) - idx), e + temp_e)
            )
            picks[i] += 1

    return min(result)


def solution(picks, minerals):
    answer = 0
    answer = mining(picks, minerals, 0, 0)
    return answer
