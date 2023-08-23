def prm(n, num, visited, numbers, number_permutation):
    if len(num) == n:
        number_permutation.add(int(num))
        return
    
    for i in range(0, len(visited)):
        if not visited[i]:
            visited[i] = True
            prm(n, num + numbers[i], visited, numbers, number_permutation)
            visited[i] = False

def solution(numbers):
    answer = 0
    n = len(numbers)
    number_permutation = set()
    visited = [False] * n
    
    # 1개 ~ n개 까지의 종이조각으로 만들 수 있는 순열 생성
    for i in range(1, n + 1):
        prm(i, "", visited, numbers, number_permutation)

    # 0과 1은 소수가 아니다 제외
    number_permutation -= {0, 1}
    
    # 소수인지 확인
    for number in list(number_permutation):
        for j in range(2, int(number ** 0.5) + 1):
            if number % j == 0:
                break
        else:
            answer += 1        
    
    return answer

