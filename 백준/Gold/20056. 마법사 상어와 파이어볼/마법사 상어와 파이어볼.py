from collections import deque

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

n, m, k = map(int, input().split())
fireballs = deque()
for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fireballs.append([r - 1, c - 1, m, s, d])

# k번 이동
for _ in range(k):
    next_fireballs = dict()
    merged_fireballs = set()

    # 기존 파이어볼 수만큼만 pop해준다(이동)
    for _ in range(len(fireballs)):
        r, c, m, s, d = fireballs.popleft()
        nr, nc = (r + s * dr[d]) % n, (c + s * dc[d]) % n

        # 동일 위치에 파이어볼이 2개 이상 들어 가는경우
        if (nr, nc) in next_fireballs:
            # 합쳐지는 파이어볼 좌표 표시
            merged_fireballs.add((nr, nc))
            next_fireballs[(nr, nc)][0] += m
            next_fireballs[(nr, nc)][1] += s
            next_fireballs[(nr, nc)][3] += 1
            # 합쳐지는 파이어 볼 방향 정하기
            if next_fireballs[(nr, nc)][2] != "odd" and next_fireballs[(nr, nc)][2] % 2 != d % 2:
                next_fireballs[(nr, nc)][2] = "odd"
        else:
            next_fireballs[(nr, nc)] = [m, s, d, 1]
    
    # 이동이 끝난 파이어볼을 파이어볼 큐에 넣어준다
    for fireball_pos in next_fireballs:
        r, c = fireball_pos
        m, s, d, cnt = next_fireballs[fireball_pos]
        # 합쳐진 파이어볼 분화
        if (r, c) in merged_fireballs:
            # 질량이 0이면 소멸
            if m // 5 == 0:
                continue
            dirs = [0, 2, 4, 6]
            if d == "odd":
                dirs = [1, 3, 5, 7]
            # 각 방향으로 분화
            for dir in dirs:
                fireballs.append([r, c, m // 5, s // cnt, dir])
        # 그냥 파이어볼은 q에 바로추가
        else:
            fireballs.append([r, c, m, s, d])

answer = 0
for fireball in fireballs:
    answer += fireball[2]
print(answer)