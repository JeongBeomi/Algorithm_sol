from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse = True))
    
    while people:
        w = people.popleft()
        if people and people[-1] + w <= limit:
            people.pop()
        answer += 1
    
    return answer