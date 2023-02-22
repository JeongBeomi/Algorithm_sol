di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]

def solution(maps):
    s_i, s_j = 0, 0
    n, m = len(maps), len(maps[0])
    
    for i in range(n):
        maps[i] = list(maps[i])
        for j in range(m):
            if maps[i][j] == "L":  
                s_i, s_j = i, j

    answer = bfs([s_i, s_j], maps, n , m)
    return sum(answer)

def bfs(s_p, miro, n, m):
    miro[s_p[0]][s_p[1]] = 0
    result = [100, 100]
    find = [False, False]
    q = [s_p]
    
    while q:
        if find[0] and find[1]:
            break
        v_i, v_j = q.pop(0)
        for i in range(4):
            n_i, n_j = v_i + di[i], v_j + dj[i]
            if (0 <= n_i < n and 0 <= n_j < m and miro[n_i][n_j] in ("O", "S", "E")):
                if miro[n_i][n_j] == "S":
                    result[0] = miro[v_i][v_j] + 1
                    find[0] = True
                elif miro[n_i][n_j] == "E":
                    result[1] = miro[v_i][v_j] + 1
                    find[1] = True
                miro[n_i][n_j] = miro[v_i][v_j] + 1
                q.append([n_i, n_j])
    else:
        return [-1]

    return result