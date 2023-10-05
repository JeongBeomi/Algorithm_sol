def solution(k, tangerine):
    answer = 0
    cnt_dict = dict()
    
    # 귤 사이즈별 카운트
    for t in tangerine:
        if t in cnt_dict:
            cnt_dict[t] += 1
        else:
            cnt_dict[t] = 1
    
    # 정렬을 위해 카운트 수 리스트 만들기
    cnt_list = list()
    for v in cnt_dict.values():
        cnt_list.append(v)
        
    cnt_list.sort(reverse = True)

    # 원하는 귤 개수 만큼 뽑기
    for cnt in cnt_list:
        k -= cnt
        answer += 1
        if k <= 0:
            break
    
    return answer