def solution(bandage, health, attacks):
    answer = health
    t = 0
    
    for attack in attacks:
        # 초당 회복량과 추가회복량
        banding_time = (attack[0] - t - 1)
        recovery = bandage[1] * banding_time
        recovery += banding_time // bandage[0] * bandage[2]
        answer = min(health, answer + recovery)
        
        # 몬스터 공격
        answer -= attack[1]
        if answer <= 0:
            answer = -1
            break
            
        t = attack[0]
        
    return answer