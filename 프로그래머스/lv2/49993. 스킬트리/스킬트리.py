def solution(skill, skill_trees):
    answer = 0
    # 배울려는 스킬의 인덱스를 빨리 찾기위해 딕셔너리로 만들어주기
    idx_dict = {k : v for v, k in enumerate(skill)}
    for skill_tree in skill_trees:
        # 지금까지 배울수 있는 스킬
        now_idx = 0
        for s in skill_tree:
            s_idx = idx_dict.get(s)
            # 스킬트리 상관없이 배울 수 있는 스킬일 때
            if s_idx == None:
                continue
            # 배울려는 스킬을 배울 수 없을 때
            if s_idx > now_idx:
                break
            # 아직 배우지는 않았으나 배울 수 있는 스킬일 때
            elif s_idx == now_idx:
                now_idx += 1
        # 정상적은 하나의 skill_tree 순회가 성공하면
        else:
            answer += 1
    return answer
