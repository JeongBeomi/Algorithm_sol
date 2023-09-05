def solution(n):
    # 하, 우 좌상향 방향 순서
    dr = [1, 0, -1]
    dc = [0, 1, -1]
    answer = []
    
    # 삼각형을 왼쪽으로 붙여 직각삼각형처럼 본다
    triangle = [[0] * (i + 1) for i in range(n)]

    # 1 시작점 및 방향 d 초기화
    r, c = 0, 0
    triangle[r][c] = 1
    d = 0
    flag = False
    while True:
        nr, nc = r + dr[d], c + dc[d]
        # 다음칸이 인덱스가 맞는지, 비어있는지 확인
        if 0 <= nr < n and 0 <= nc <= nr and triangle[nr][nc] == 0:
            triangle[nr][nc] = triangle[r][c] + 1
            r, c = nr, nc
            flag = False

        # 유효하지 않은칸이면 방향바꿔서 다시 확인    
        else:
            # 이전 루프에서 한번 방향을 바꿧는데 또 유효하지 않으면 더이상 채울곳이 없다
            if flag:
                break
            d = (d + 1) % 3
            flag = True
            
    
    for line in triangle:
        answer += line
        
    return answer