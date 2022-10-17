def solution(price, money, count):
    answer = price * ((1 + count) * count / 2) - money
    return answer if answer > 0 else 0