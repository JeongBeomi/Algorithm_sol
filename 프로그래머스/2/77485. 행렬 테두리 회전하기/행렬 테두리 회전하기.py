def solution(rows, columns, queries):
    answer = []
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    num_map = [[r * columns + c for c in range(1, columns + 1)] for r in range(rows)] 
    
    for query in queries:
        # l_ 최소 row, column, m_최대 row, column
        lr, lc, mr, mc = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1
        min_num = num_map[lr][lc]
        num_map[lr][lc], temp = num_map[lr + 1][lc], num_map[lr][lc]
        
        # 시작좌표(temp에 시작좌표를 넣기 때문에 시작은 한칸 옆에서 시작), 방향
        r, c, d = lr, lc + 1, 0
        
        # 최소 좌표로 오면 회전 끝
        while r != lr or c != lc:
            # 최소값 갱신
            if min_num > num_map[r][c]:
                min_num = num_map[r][c]
            num_map[r][c], temp = temp, num_map[r][c]
            nr, nc = r + dr[d], c + dc[d]
            if lr <= nr <= mr and lc <= nc <= mc:
                r, c = nr, nc
            else:
                d += 1
                r, c = r + dr[d], c + dc[d]
        answer.append(min_num)
    return answer
