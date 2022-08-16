for _ in range(10):
    tc = int(input())
    string_list = [input() for _ in range(100)]
    max_cnt = 1

    # 가장 긴 회문을 찾기 때문에 길이 100인 회문 부터 찾기 시작
    for i in range(100, 2, -1):
        # 가장 긴 길이 100부터 시작하기 때문에 회문을 찾는 순간 더이상 찾을 필요 없음.
        if max_cnt > 1:
            break
        # 가로 탐색 길이 i인 회문 검사
        for string_line in string_list:
            for j in range(0, 100 - i + 1):
                if string_line[j:j + i] == string_line[j:j + i][::-1]:
                    max_cnt = i
        # 세로 탐색 길이 i인 회문 검사
        for new_string_line in zip(*string_list):
            for k in range(0, 100 - i + 1):
                if new_string_line[k:k + i] == new_string_line[k:k + i][::-1]:
                    max_cnt = i
    print(f"#{tc} {max_cnt}")