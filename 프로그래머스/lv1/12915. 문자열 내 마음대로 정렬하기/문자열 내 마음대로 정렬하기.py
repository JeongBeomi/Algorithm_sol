def solution(strings, n):
    strings.sort(key = lambda x : [x[n]] + [x[i] for i in range(0, n)] + [x[j] for j in range(n + 1, len(x))])
    return strings