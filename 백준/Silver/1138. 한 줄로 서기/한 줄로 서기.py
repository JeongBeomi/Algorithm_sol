n = int(input())
cnt_list = list(map(int, input().split()))
line = [0] * n

for i in range(n):
    taller_cnt = cnt_list[i]
    # 본인 자리 기준 앞에는 키가 큰 사람 수만큼 빈자리가 있어야한다.
    empty_cnt = 0
    for j in range(n):
        # 만약 자리에 주인이 있으면 넘어간다
        if line[j] != 0:
            continue
        # 자리가 비어있으면 자기자리인가 확인후 맞으면 착석
        if empty_cnt == taller_cnt:
            line[j] = i + 1
            break

        empty_cnt += 1


print(*line)
