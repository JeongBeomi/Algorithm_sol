# c개의 원소로 이루어진 조합 만드는 함수
def comb(alpa, c, start, word, comb_list):
    if len(word) == c:
        comb_list.append(word)
        return
    
    for i in range(start, len(alpa)):
        word += alpa[i]
        comb(alpa, c, i + 1, word, comb_list)
        word = word[:-1]        

# comb코스가 몇번 주문되었는지 카운트하는 함수
def check_order(order_list, m):
    result = 0
    for order in order_list:
        # m코스에 포함된 알파벳이 포함되어있는지 확인
        for c in m:
            if c not in order:
                break
        # 정상적으로 반복을 마치면 모두 포함되어있는 것이기 때문에 주문카운트  + 1
        else:
            result += 1
    return result    
        
def solution(orders, course):
    answer = []
    alpa = set()

    for c in course:
        # course 값만큼의 개수를 가지는 조합 만들기
        comb_list =  []
        for i in range(len(orders)):
            comb(sorted(orders[i]), c, 0, "", comb_list)
            # in연산을 위해 set 자료형으로 변경
            orders[i] = set(orders[i])
            
        comb_list = list(set(comb_list))
        # 인덱스가 주문 횟수 value는 해당 인덱스만큼 주문된 메뉴 목록
        cnt_list = [[] for _ in range(len(orders) + 1)]
        max_cnt = 0
        # 코스요리 메뉴 주문 횟수 찾기
        for i in range(len(comb_list)):
            cnt = check_order(orders, comb_list[i])
            if cnt >= max_cnt:
                cnt_list[cnt].append(comb_list[i])
                max_cnt = cnt
        if max_cnt >= 2:
            answer += cnt_list[max_cnt]
                
    answer.sort()
    return answer