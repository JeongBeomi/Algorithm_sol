def solution(land):
    answer = 0
    land_length = len(land)
    memo = [[0, 0, 0, 0] for _ in range(land_length)]
    memo[0] = [n for n in land[0]]
    
    # land의 N개의 행을 완전탐색할 것이다.
    for i in range(1, land_length):
        # i번 land에서 선택할 수있는 땅은 총 4개
        for j in range(0, 4):
            max_num = 0
            # 위 반복문에서 선택한 땅과 이전 선택 땅의 누적합 중 큰것을 찾아서 현재땅까지의 최대값 도출
            for k in range(0, 4):
                # 위에서 선택한 j 와 같은 k땅은 선택할 수 없다 연속선택불가 조건
                if k == j:
                    continue
                # i번째 land에서 j번째땅을 선택할 경우 3가지 경우중 가장 큰값을 구한다
                if land[i][j] + memo[i - 1][k] > max_num:
                    max_num = memo[i - 1][k] + land[i][j]
            memo[i][j] = max_num
    answer = max(memo[-1])
    return answer