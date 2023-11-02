def solution(w,h):
    answer = 0
    num1, num2 = w, h
    # w, h의 최대공약수로 나눈 사각형이 최대공약수 만큼 반복된다 -> 최대공약수 찾아서 최소비율 사각형 찾기
    while num1 % num2 != 0:
        num1, num2 = num2, num1 % num2
    gcd = num2
    # 최소 비율 사각형에서 대각선으로 인해 잘리는 사각형 찾기
    min_w, min_h = w // gcd, h // gcd
    # 좌측 최상단 점에서 우측 최하단 점으로 가는 노드의 개수와 동일
    unusable = min_w + min_h - 1
    
    answer = w * h - unusable * gcd
    
    return answer