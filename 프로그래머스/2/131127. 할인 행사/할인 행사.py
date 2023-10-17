def solution(want, number, discount):
    answer = 0
    # 첫번째날부터 열번째날까지 할인하는 품목 딕셔너리 만들기
    discount_dict = {k : 0 for k in set(discount)}
    for i in range(10):
        discount_dict[discount[i]] += 1
        
    start_d = 1
    while True:
        # 원하는 물건을 다 구매할 수 있는지 확인
        for want_idx in range(len(want)):
            if want[want_idx] not in discount_dict or number[want_idx] > discount_dict[want[want_idx]]:
                break
        # 반복문이 정상적으로 다 실행되면 모두 구매 가능하다
        else:
            answer += 1
            
        # 할인 시작날짜를 하루 미루고 할인 행사가 유지가능한지 확인
        start_d += 1
        if len(discount) < start_d + 9:
            break
        
        # 품목 업데이트
        discount_dict[discount[start_d - 2]] -= 1
        discount_dict[discount[start_d + 8]] += 1
        
    return answer