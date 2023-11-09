def check_prime(num):
    if num == 0 or num == 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    
    return True

def solution(n, k):
    answer = 0
    # k진수로 바꿔주기
    jinso = ""
    while n != 0:
        jinso = str(n % k) + jinso
        n = n // k
    # 0을 기준으로 분리
    num_list = jinso.split("0")
    num_list.sort(key = lambda x : (len(x), x), reverse = True)
    # 아리토스테네스의 체의 경우 길이가 너무 커지면 런타임 에러 주의
    # 소수인지 확인
    for num in num_list:
        if num != "" and check_prime(int(num)):
            answer += 1
                    
    return answer