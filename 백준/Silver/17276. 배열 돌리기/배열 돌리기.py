t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    # 4가지 대각선 좌표들을 미리 만들어 준다
    pos_list = [[(i, i) for i in range(n)],
                [(i, n // 2) for i in range(n)],
                [(i, n - 1 - i) for i in range(n)],
                [(n // 2, n - 1 - i) for i in range(n)]]
    
    arr = [list(map(int, input().split())) for _ in range(n)]

    # 시계방향, 반시계방향에 따라 바꾸는 방향 달라짐
    s, e, u = 1, 5, 1
    if d < 0:
        s, e, u = 7, 3, -1
    
    # 45도씩 여러번 회전
    for _ in range(abs(d) // 45):
        temp = [arr[pos[0]][pos[1]] for pos in pos_list[0]]
        # 45도 회전시키기
        for i in range(s, e, u):
            # 바꿀좌표를 구한다 단, i가 4부터는 미리만든 대각선 좌표의 역방향
            change_idx = pos_list[i % 4]
            if i // 4 == 1:
                change_idx = change_idx[::-1]
            # 한 좌표씩 바꾸기
            for j in range(n):
                temp[j], arr[change_idx[j][0]][change_idx[j][1]] = arr[change_idx[j][0]][change_idx[j][1]], temp[j]

    for line in arr:
        print(*line)
