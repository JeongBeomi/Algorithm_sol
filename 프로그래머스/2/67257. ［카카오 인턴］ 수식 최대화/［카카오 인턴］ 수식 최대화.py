from itertools import permutations
from collections import deque

calcul_dict = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
}


def calcul(cnt, per_list, expression):
    if cnt >= 3:
        return int(expression)

    p = per_list[cnt]
    expression_list = expression.split(p)
    result = calcul(cnt + 1, per_list, expression_list[0])

    for idx in range(1, len(expression_list)):
        result = calcul_dict[p](result, calcul(cnt + 1, per_list, expression_list[idx]))

    return result


def solution(expression):
    answer = 0
    for per_list in permutations(["+", "-", "*"]):
        calcul_num = abs(calcul(0, per_list, expression))
        if answer < calcul_num:
            answer = calcul_num
    return answer