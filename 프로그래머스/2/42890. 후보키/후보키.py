from itertools import combinations

def solution(relation):
    r, c = len(relation), len(relation[0])
    candidate_keys = []
    
    # 부분집합 원소의 수 반복
    for i in range(1, c + 1):
        # 정해진 원소의 수로 이루어진 부분집합 반복
        for comb in combinations(range(c), i):
            # 유일성 확인
            unique = set()
            for j in range(r):
                value_str = ""
                for idx in comb:
                    value_str += relation[j][idx]
                unique.add(value_str)
                if len(unique) < j + 1:
                    break
            # 최소성 확인
            else:
                comb_set = set(comb)
                for candidate_key in candidate_keys:
                    # 최소성 위배
                    if candidate_key.issubset(comb_set):
                        break
                else:
                    candidate_keys.append(comb_set)
                        
    return len(candidate_keys)