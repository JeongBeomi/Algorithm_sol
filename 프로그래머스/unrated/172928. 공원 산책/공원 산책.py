d = {
    "N" : (-1, 0),
    "S" : (1, 0),
    "W" : (0, -1),
    "E" : (0, 1)
}

def walking(park_map, route, now_pos):
    direction, n = route.split()
    n = int(n)
    dr, dc = d[direction]
		# 이동지점이 park 범위를 벗어나는지 확인
    if 0 <= now_pos[0] + dr * n < len(park_map) and 0 <= now_pos[1] + dc * n < len(park_map[0]):
				# 최종 이동지점이 park범위 안이니까 한칸씩 움직이며 가는길에 X가 있는지 확인해야 한다.
        for i in range(1, n + 1):
						# i에 따라 1칸 2칸 3칸 한칸씩 이동
            nr, nc = now_pos[0] + dr * i, now_pos[1] + dc * i
            if park_map[nr][nc] == "X":
                break
				# for문을 다돌았음에도 불구하고 X를 만나지못했다면 최종이동 지점까지 이동
        else:
            now_pos = [now_pos[0] + dr * n, now_pos[1] + dc * n]
		# 다음 route 이동을 위해 현재 위치 반환
    return now_pos
    

def solution(park, routes):
    s_pos = [0, 0]
		# 시작점을 찾기 위해 park 순회
    for row in range(len(park)):
        col = park[row].find("S")
        if col != -1:
            s_pos = [row, col]
            break
    
    for route in routes:
				# 반환받은 위치로 위치 갱신
        s_pos = walking(park, route, s_pos)
    return s_pos