def solution(n, k):
    answer = []
    total_cnt = 1
    num_list = list(range(1, n + 1))
    for i in range(1, n + 1):
        total_cnt *= i
    # 인덱스 연산을 위해 -1
    k = k - 1
    
    # 맨 앞자리 숫자부터 하나씩 찾을 예정
    while len(answer) < n:
        # 하나의 자리수가 책임지는 경우의 수 개수는 만들 수 있는 전체 경우의 수 개수 // 원소 개수
        total_cnt = total_cnt // len(num_list)
        # 몫이 사용하는 숫자의 인덱스
        answer.append(num_list.pop(k // total_cnt))
        # 다음 숫자를 찾기 위해 k 갱신
        k = k % total_cnt
        
    return answer
