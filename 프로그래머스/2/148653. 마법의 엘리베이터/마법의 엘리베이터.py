def solution(storey):
    answer = 0
    # 1의자리부터 해결해간다
    while storey > 0:
        storey, num = storey // 10, storey % 10
        # 5보다 크면 +10^c 로 올라가서 -10^c+1로 내려오는게 적은 횟수
        if num > 5:
            answer += 10 - num
            storey += 1
        # 5보다 작으면 내려가는게 최소 횟수
        elif num < 5:
            answer += num
        # 5일 때는 다음 자리 수가 5이상일 때는 올라가고 아니면 내려간다
        elif num == 5:
            if storey % 10 >= 5:
                answer += 10 - num
                storey += 1
            else:
                answer += num
    return answer