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
    if 0 <= now_pos[0] + dr * n < len(park_map) and 0 <= now_pos[1] + dc * n < len(park_map[0]):
        for i in range(1, n + 1):
            nr, nc = now_pos[0] + dr * i, now_pos[1] + dc * i
            if park_map[nr][nc] == "X":
                break
        else:
            now_pos = [now_pos[0] + dr * n, now_pos[1] + dc * n]
    return now_pos
    

def solution(park, routes):
    s_pos = [0, 0]
    for row in range(len(park)):
        col = park[row].find("S")
        if col != -1:
            s_pos = [row, col]
            break
    
    for route in routes:
        s_pos = walking(park, route, s_pos)
        print(s_pos)
    return s_pos