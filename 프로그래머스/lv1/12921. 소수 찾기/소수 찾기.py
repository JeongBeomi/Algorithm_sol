# 인덱스 0 은버리고, 인덱스 1부터는 1부터 인덱스사이 수 소수 개수 
memo = [0, 0]
def solution(n):
    answer = 0
    cnt = len(memo)
    # 지금까지 기록한 수 범위 안이면 바로 출력
    if cnt >= n + 1:
        return memo[n]
    # 기록해놓은 범위 넘어가면 추가해주기
    else:
        for num in range(cnt, n + 1):
            # 1가 본인 자신을 제외한 약수가 존재하지 않으면 소수
            for i in range(2, int(num ** (1/2)) + 1):
                # 2 ~ 해당숫자 ** 1/2 사이에서 하나라도 나누어떨이지면 소수가 아니다
                if num % i == 0:
                    memo.append(memo[num - 1])
                    break
            # 소수라면 전 갯수 + 1로 저장
            else:
                memo.append(memo[num - 1] + 1)

    return memo[n]