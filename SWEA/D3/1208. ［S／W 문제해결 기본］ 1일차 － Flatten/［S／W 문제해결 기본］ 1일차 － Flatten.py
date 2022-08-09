for tc in range(10):
    dump_cnt = int(input())
    dump_map = list(map(int, input().split()))

    while dump_cnt:
        max_idx = 0
        min_idx = 0
        
        # 최저 최고 높이 지점 찾기
        for idx in range(1, 100):
            if dump_map[max_idx] < dump_map[idx]:
                max_idx = idx
            elif dump_map[min_idx] > dump_map[idx]:
                min_idx = idx

        # 덤프 실행 전 최저 최고 높이차이가 1이하면 더이상 덤프 처리할 필요가 없음.
        if (dump_map[max_idx]-dump_map[min_idx]) <= 1:
            break

        # 덤프 실행
        dump_map[max_idx] -= 1
        dump_map[min_idx] += 1
        dump_cnt -= 1
        
    max_idx = 0
    min_idx = 0
    for idx in range(1, 100):
        if dump_map[max_idx] < dump_map[idx]:
            max_idx = idx
        elif dump_map[min_idx] > dump_map[idx]:
            min_idx = idx

    print(f"#{tc+1} {dump_map[max_idx]-dump_map[min_idx]}")
