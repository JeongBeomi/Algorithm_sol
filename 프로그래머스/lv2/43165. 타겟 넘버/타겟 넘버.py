from collections import deque

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    # (현재까지 계산 결과, numbers에서 몇번째 인덱스 까지 사용했는지)
    q = deque([(numbers[0], 0), (-numbers[0], 0)])
    while q:
        result, idx = q.popleft()
        # numbers의 모든인덱스를 다 거쳐갔다면 목표숫자와 같은지 확인
        if idx == n - 1:
            if result == target:
                answer += 1
            continue
        # 다음 인덱스의 값을 + or - 추가해주기
        q.append((result + numbers[idx + 1], idx + 1))
        q.append((result - numbers[idx + 1], idx + 1))
        
    return answer