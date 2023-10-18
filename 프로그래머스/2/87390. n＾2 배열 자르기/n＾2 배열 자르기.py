def solution(n, left, right):
    # i를 통해 row, column을 알 수 있다. 해당자리는 r,c 중 최대값 + 1이 된다
    answer = [max(i // n, i % n) + 1 for i in range(left, right + 1)]
    return answer