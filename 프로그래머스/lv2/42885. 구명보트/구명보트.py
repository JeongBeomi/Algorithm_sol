def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    
    # 처음과 끝
    s, e = 0, len(people) - 1
    while s <= e:
        # 제한무게 이하라서 두개 빠지면 e도 옮겨주기
        if people[s] + people[e] <= limit:
            e -= 1
        
        s += 1
        answer += 1
    return answer