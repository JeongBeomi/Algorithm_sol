def solution(prices):
    n = len(prices)
    answer = []
    for i in range(n):
        s = n - i - 1
        for j in range(i + 1, n):
            if prices[i] > prices[j]:
                s = j - i
                break
        answer.append(s)
    return answer