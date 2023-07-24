# d = {
#     "N" : (-1, 0),
#     "S" : (1, 0),
#     "W" : (0, -1),
#     "E" : (0, 1)
# }

# def walking(park_map, route, now_pos):
#     direction, n = route.split()
#     n = int(n)
#     dr, dc = d[direction]
#     if 0 <= now_pos[0] + dr * n < len(park_map) and 0 <= now_pos[1] + dc * n < len(park_map[0]):
#         for i in range(1, n + 1):
#             nr, nc = now_pos[0] + dr * i, now_pos[1] + dc * i
#             if park_map[nr][nc] == "X":
#                 break
#         else:
#             now_pos = [now_pos[0] + dr * n, now_pos[1] + dc * n]
#     return now_pos
    

# def solution(park, routes):
#     s_pos = [0, 0]
#     for row in range(len(park)):
#         col = park[row].find("S")
#         if col != -1:
#             s_pos = [row, col]
#             break
    
#     for route in routes:
#         s_pos = walking(park, route, s_pos)
#     return s_pos

def solution(park, routes):
    answer = []
    # 동 남 서 북 
    dir = {'E': (0,1), 'S':(1,0),'W':(0,-1), 'N':(-1,0)}
    
    for i in range(len(park)):
        for j in range(len(park[i])):
            # 시작점 찾아서 시작! 
            if park[i][j] == 'S':
                for k in range(len(routes)):
                    # 나중 예외처리를 위해
                    x,y = i,j
                    d, cnt = routes[k].split()
                    # 거리만큼 반복
                    for l in range(int(cnt)):
                        nx, ny = dir[d][0]+i, dir[d][1]+j
                        # 조건 부합 -> 방향으로 1거리씩 이동
                        if 0<= nx< len(park) and 0<= ny < len(park[i]) and park[nx][ny] != "X": 
                            i,j = nx, ny
                        # 중간에 잘못된 경우, 이전으로 되돌리고 종료
                        else:
                            i,j = x,y
                            break
                return [i,j]