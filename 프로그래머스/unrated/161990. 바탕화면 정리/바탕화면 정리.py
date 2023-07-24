def solution(wallpaper):
    answer = []
    lux, luy, rdx, rdy = 50, 50, 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                lux, luy, rdx, rdy = min(i, lux), min(j, luy), max(i, rdx), max(j, rdy)
    answer = [lux, luy, rdx + 1, rdy + 1]
    return answer