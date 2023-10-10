# def solution(elements):
#     answer = 0
#     n = len(elements)
#     num_set = set()
#     num_list = [0] * n
#     # 각 인덱스를 시작점으로 숫자를 하나씩 더해간다
#     for i in range(n):
#         for j in range(n):
#             num_list[j] += elements[(j + i) % n]
#             num_set.add(num_list[j])
#     answer = len(num_set)
#     return answer

def solution(elements):
    ll = len(elements)
    res = set()

    for i in range(ll):
        ssum = elements[i]
        res.add(ssum)
        for j in range(i+1, i+ll):
            ssum += elements[j%ll]
            res.add(ssum)
    return len(res)