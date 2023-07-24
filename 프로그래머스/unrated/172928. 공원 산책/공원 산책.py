def solution(park, routes):
    park = [list(p) for p in park]

    # 방향
    direction = 'NSWE'
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    t_x, t_y= 0, 0
    for x in range(len(park)):
        for y in range(len(park[x])):
            if park[x][y] == 'S':          # 시작점 찾기
                nx, ny = x, y
                t_x, t_y = x, y

                for route in routes:       # 이동 방향 더해주기
                    op, n = route.split()  # d, n : 이동방향, 이동칸수
                    i = direction.find(op)
                    for _ in range(int(n)): # 이동칸수만큼 이동
                        nx += dx[i] # 이동 
                        ny += dy[i] # 이동

                        if nx > len(park)-1 or ny > len(park[0])-1 or nx < 0 or ny < 0 or park[nx][ny] == 'X': # 장애물이 있을 때, 범위가 넘어갈때
                            nx, ny = t_x, t_y
                            break
                    t_x, t_y = nx, ny  # x, y에 이동할 nx, ny를 넣어준다
             

    return [t_x, t_y]