from heapq import heappush, heappop

def solution(n, k, enemy):
    answer = 0
    heap_q = []
    
    for e in enemy:
        n -= e
        heappush(heap_q, -e)
        # 병사 부족할 때 무적권 있는지 확인
        if n < 0:
            # 무적권이 존재하면 이번판을 포함해 진행한 게임에서 가장 적인원이 많은 경우를 무적권 사용
            if k > 0:
                n += -heappop(heap_q)
                k -= 1
            # 무조권 없으면 게임 끝
            else:
                break
        
        answer += 1
    
    return answer