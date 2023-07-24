def solution(wallpaper):
    answer = []
    x_list, y_list = [], []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                x_list.append(i)
                y_list.append(j)
    x_list.sort()
    y_list.sort()
    answer = [x_list[0], y_list[0], x_list[-1] + 1, y_list[-1] + 1]
    
    return answer
