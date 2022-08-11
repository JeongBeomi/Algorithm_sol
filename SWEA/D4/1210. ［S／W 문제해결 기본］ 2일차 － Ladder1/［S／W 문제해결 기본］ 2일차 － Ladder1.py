
# 델타 이동 좌-우-상
di = [0, 0, -1]
dj = [-1, 1, 0]
now_dir = 2
for _ in range(10):
    n = int(input())
    ladder_map = [list(map(int, input().split())) for _ in range(100)]

    # 도착지점 i, j 인덱스 찾아서 현재위치로 지정
    for search_idx in range(100):
        if ladder_map[99][search_idx] == 2:
            now_i = 99
            now_j = search_idx
    while now_i > 0:

        # 현재 진행 방향이 상 이면 좌우 길이 있는지 확인
        if now_dir == 2:
            for side_idx in range(2):
                ni = now_i + di[side_idx]
                nj = now_j + dj[side_idx]
                # 좌, 우방향으로 이동 가능하면 현재 방향을 이동가능한 방향으로 변경 이동
                if 0 <= nj < 100 and ladder_map[ni][nj] == 1:
                    now_dir = side_idx
                    now_i, now_j = ni, nj
                    break
            now_i = now_i + di[now_dir]
            now_j = now_j + dj[now_dir]

        #현재 진행 방향이 좌/우면 끝가지 이동후 현재 진행방향 상으로 변경 후 한칸이동
        else:
            while True:
                ni = now_i + di[now_dir]
                nj = now_j + dj[now_dir]

                if not(0 <= nj < 100) or ladder_map[ni][nj] == 0:
                    now_dir = 2
                    now_i = now_i + di[now_dir]
                    now_j = now_j + dj[now_dir]
                    break
                now_i, now_j = ni, nj
    print(f"#{n} {now_j}")