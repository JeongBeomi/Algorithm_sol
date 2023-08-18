dr = (0, 1, 1) 
dc = (1, 1, 0)

def fourblock(r, c, arr):
    t = arr[r][c]
    positions = [(r, c)]
    for d in range(3):
        nr, nc = r + dr[d], c + dc[d]
        if 0 <= nr < len(arr) and 0 <= nc < len(arr[0]) and arr[nr][nc] == t:
            positions.append((nr, nc))
        # 하나라도 좌표를 벗어나거나 다른 블록이 나오면 탈출
        else:
            positions = []
            break
    
    return positions
    

def solution(m, n, board):
    answer = 0
    global exist
    # row가 세로방향인 리스트로 새로만들기
    new_board = list(map(list, zip(*board[::-1])))
    
    while True:
        # 전체 맵을 한번보고 더이상 지워지는 블록이 없으면 탈출을 위해 표시
        exist = False
        # 순회하며 4칸이같은지 확인하고 지울 칸들 erase_pos에 추가 
        erase_pos = set()
        for i in range(n):
            for j in range(m):
                if new_board[i][j] != "":
                    result = fourblock(i, j, new_board)
                    if result:
                        for r in result:
                            erase_pos.add(r)
                        exist = True
            
        # 블록 지우기
        for e_r, e_c in list(erase_pos):
            new_board[e_r][e_c] = ""
            answer += 1
        
        # 블록 내리기
        for line_idx in range(n):
            # 삭제된 칸을 제외하고 내려서 리스트 만들기
            temp = list("".join(new_board[line_idx]))
            # 인덱스 에러 방지를 위해 칸수에맞게 빈칸 추가해주기
            temp += [""] * (m - len(temp))
            new_board[line_idx] = temp
        
        # 더이상 지워질 블록이 없으면 탈출
        if not exist:
            break
            
    return answer
