from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque()
    total_weight = 0
    while truck_weights or bridge:
        answer += 1
        # 다리에서 트럭이 빠지는지 확인
        if bridge and answer - bridge[0][1] == bridge_length:
            total_weight -= bridge[0][0]
            bridge.popleft()
            
        # 새로운 트럭이 다리로 올라가는지 확인
        if truck_weights and len(bridge) < bridge_length and total_weight + truck_weights[0] <= weight:
            w = truck_weights.popleft()
            total_weight += w
            bridge.append((w, answer))
            
    return answer