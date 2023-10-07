def solution(n):
    answer = 0
    dp = [0, 1, 2]    
    while len(dp) <= n:
        dp.append(dp[-1] + dp[-2])
    answer = dp[n] % 1234567
    return answer