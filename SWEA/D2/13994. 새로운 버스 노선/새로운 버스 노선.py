t = int(input())
for tc in range(t):
    n = int(input())
    stop_cnt = [0] * 1001
    for _ in range(n):
        bus, a, b = map(int, input().split())
        stop_cnt[a] += 1
        stop_cnt[b] += 1
        if bus == 1:    # 일반
            for i in range(a + 1, b):
                stop_cnt[i] += 1
        elif bus == 2:  # 급행
            for i in range(a + 2, b, 2):
                stop_cnt[i] += 1
        else:
            for i in range(a + 1, b):
                if a % 2 == 0 and i % 4 == 0:
                    stop_cnt[i] += 1
                elif a % 2 == 1 and i % 3 == 0 and i % 10 != 0:
                    stop_cnt[i] += 1
    print(f"#{tc + 1} {max(stop_cnt)}")