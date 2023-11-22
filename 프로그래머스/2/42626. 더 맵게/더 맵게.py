import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2:
        if scoville[0] >= K:
            break
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        answer += 1
    else:
        if scoville[0] < K:
            answer = -1
    return answer