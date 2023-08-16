def solution(nums):
    answer = 0
    n = len(nums)
    max_sum = sum(sorted(nums)[n - 3 : n])
    
    # 아리토스테네스의 체
    check_set = set(range(max_sum + 1))
    # 제일최근 값 ** 0.5 이후는 그전수의 배수로 생각안해도된다.
    for i in range(2, int(max_sum ** (1/2) + 1)):
        if i in check_set:
            check_set -= set(range(2 * i, max_sum + 1, i))
                             
    # nums 중 세개 조합 combination 사용하면 더욱간단 범위는 3개이상 남아야한다
    num_sum = 0
    for j in range(n - 2):
        num_sum += nums[j]
        for k in range(j + 1, n - 1):
            num_sum += nums[k]
            for m in range(k + 1, n):
                num_sum += nums[m]
                if num_sum in check_set:
                    answer += 1
                num_sum -= nums[m]
            num_sum -= nums[k]
        num_sum -= nums[j]
    
    return answer
