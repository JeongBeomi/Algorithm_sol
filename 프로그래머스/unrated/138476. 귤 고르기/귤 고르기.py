# def recur(cnt_dict, k, cnt, now_idx, answer):
#     if answer[0] <= cnt:
#         return
    
#     if k <= 0:
#         answer[0] = min(answer[0], cnt)
#         return
    
#     cnt_keys = list(cnt_dict.keys())
#     for i in range(now_idx, len(cnt_dict)):
#         recur(cnt_dict, k - cnt_dict[cnt_keys[i]], cnt + 1, i + 1, answer)

def solution(k, tangerine):
    sizes = list(set(tangerine))
    answer = 0
    cnt_dict = dict()
    
    # 귤 사이즈별 카운트
    for t in tangerine:
        if t in cnt_dict:
            cnt_dict[t] += 1
        else:
            cnt_dict[t] = 1
    
    cnt_list = list()
    for i, v in cnt_dict.items():
        cnt_list.append((i, v))
        
    cnt_list.sort(key = lambda x : -x[1])

    for t, cnt in cnt_list:
        k -= cnt
        answer += 1
        if k <= 0:
            break
    
    return answer