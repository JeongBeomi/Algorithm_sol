from collections import deque

def solution(x, y, n):
    answer = -1
    # 연산을 위한 lambda 딕셔너리
    cal_dict = {
        0 : lambda x : x + n,
        1 : lambda x : x * 2,
        2 : lambda x : x * 3
    }
    # BFS를 위한 스택과 방문체크를 위한 셋
    s = deque([(x, 0)])
    visited = {x}
    
    while s:
        num, cnt = s.popleft()
        # num 이 목표한 수랑 같으면 탈출
        if num == y:
            answer = cnt
            break
            
        for i in range(3):
            n_num = cal_dict[i](num)
            # 커지는 연산뿐이없으니까 y 보다 작거나 같아야하고, 방문한적이 없어야한다
            if n_num <= y and n_num not in visited:
                s.append((n_num, cnt + 1))
                visited.add(n_num)
    

    return answer