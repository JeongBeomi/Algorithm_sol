def check(i, j, like_students):
    like_cnt = 0
    blank_cnt = 0
    for d in range(4):
        ni, nj = i + dr[d], j + dc[d]
        if 0 <= ni < n and 0 <= nj < n:
            # 인접한 칸이 빈자리일때
            if seats[ni][nj] == 0:
                blank_cnt += 1
            # 인접한 칸에 좋아하는 친구가 앉아 있는 경우
            elif seats[ni][nj] in like_students:
                like_cnt += 1
    # 우선 순위 순서대로 튜플 만들어서 반환
    return (like_cnt, blank_cnt, i, j)

dr = (0, 0, -1, 1)
dc = (-1, 1, 0, 0)

n = int(input())
# 상어를 채울 좌석 배열
seats = [[0] * n for _ in range(n)]
answer = 0
# 나중에 만족도 측정을 위해 좋아하는 친구 딕셔너리 만들기
like_dict = dict()
# 좌석 채우기
for _ in range(n ** 2):
    student_num, *like_students = map(int, input().split())
    like_students = set(like_students)
    like_dict[student_num] = like_students
    seat_info = (0, 0, n, n)
    
    # 전체 좌석중 비어있는 좌석에서 좋아하는 인접 학생수, 비어있는 인접칸 등 조건 확인
    for i in range(n):
        for j in range(n):
            if seats[i][j] == 0:
                # 조건 우선순위를 고려하여 정렬하여 가장적합한 자리 선정
                seat_info = sorted([seat_info, check(i, j, like_students)], key = lambda x : (-x[0], -x[1], x[2], x[3]))[0]
    
    # 전체 좌석중 가장적합한 자리에 앉히기
    seats[seat_info[2]][seat_info[3]] = student_num

# 좌석중 친한친구 카운트 더해주기
for r in range(n):
    for c in range(n):
        temp = 0
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and seats[nr][nc] in like_dict[seats[r][c]]:
                temp += 1
        if temp != 0:
            answer += 10 ** (temp - 1)

print(answer)