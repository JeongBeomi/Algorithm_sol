def solution(number, limit, power):
    answer = 0
    for num in range(1, number + 1):
        # 약수 중복 방지를 위해 set
        divisor_set = set()
        # 약수 구하기
        for i in range(1, int(num ** (1/2)) + 1):
            if num % i == 0:
                divisor_set.add(i)
                divisor_set.add(num // i)
        # 철의 무게 계산
        answer += power if len(divisor_set) > limit else len(divisor_set)
        
    return answer