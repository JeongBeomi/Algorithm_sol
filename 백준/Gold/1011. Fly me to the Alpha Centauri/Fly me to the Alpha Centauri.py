test_case = int(input())
for _ in range(test_case):
    x_point, y_point = map(int, input().split())
    total_move_len = y_point - x_point
    move_len = 1
    move_count = 0
    while True:
        if total_move_len > (move_len * 2):
            total_move_len -= move_len * 2
            move_len += 1
            move_count += 2
        elif total_move_len > move_len:
            move_count += 2
            break
        else:
            move_count += 1
            break
    print(move_count)
