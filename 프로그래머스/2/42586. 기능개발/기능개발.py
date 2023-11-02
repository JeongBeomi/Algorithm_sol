def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    idx = 0
    d = 0
    while idx < n:
        # d일만큼 지났을 때 현재 작업 진도가 100%가 안될때 100%가 되는 만큼 시간 경과
        if progresses[idx] + d * speeds[idx] < 100:
            d = (100 - progresses[idx]) // speeds[idx]
            if (100 - progresses[idx]) % speeds[idx] != 0:
                d += 1
            answer.append(1)
        # 작업 진행도가 100% 이상일때 다음으로 넘어감
        else:
            answer[-1] += 1
        
        idx += 1
        
    return answer