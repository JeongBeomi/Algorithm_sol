def solution(dirs):
    answer = 0
    # 좌표 이동은 0,0 -> 2, 0이라고 생각하고 1, 0 좌표는 이동경로로 생각한다. 
    d_dict = {"U" : (0, 2), "D" : (0, -2), "R" : (2, 0), "L" : (-2, 0)}
    check_set = set()
    x, y = 0, 0
    for dir in dirs:
        nx, ny = x + d_dict[dir][0], y + d_dict[dir][1]
        # 좌표평면 안에 존재하는지 확인
        if -10 <= nx <= 10 and -10 <= ny <= 10:
            # 한번도 지나가지 않은 경로일 때
            if ((x + nx)//2, (y + ny)//2) not in check_set:
                check_set.add(((x + nx)//2, (y + ny)//2))
                answer += 1
            x, y = nx, ny
    
    return answer