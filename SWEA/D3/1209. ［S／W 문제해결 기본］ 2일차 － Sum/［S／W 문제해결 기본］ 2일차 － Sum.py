
for _ in range(10):
    n = int(input())
    numbers_list = [list(map(int, input().split())) for _ in range(100)]
    max_result = 0

    cross_sum = 0
    reverse_cross_sum = 0
    for i in range(100):
        cross_sum += numbers_list[i][i]
        reverse_cross_sum += numbers_list[i][99-i]
        x_line_sum = 0
        y_line_sum = 0
        for j in range(100):
            # 각 행의 합 x_line_sum
            x_line_sum += numbers_list[i][j]
            # 각 열의 합 y_line_sum
            y_line_sum += numbers_list[j][i]

        # 각 열과 행의 최대값 확인
        if x_line_sum > max_result:
            max_result = x_line_sum
        if y_line_sum > max_result:
            max_result = y_line_sum
    # 대각성 방향에세 최대값 확인
    if cross_sum > max_result:
        max_result = cross_sum
    if reverse_cross_sum > max_result:
        max_result = reverse_cross_sum

    print(f"#{n} {max_result}")