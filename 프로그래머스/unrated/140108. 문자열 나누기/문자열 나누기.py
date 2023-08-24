def solution(s):
    answer = 0
    n = len(s)
    
    target = ""
    cnt1, cnt2 = 0, 0
    for i in range(n):
        # 첫글자 읽기
        if not target:
            target = s[i]
            cnt1 += 1
            continue
        # 같은 글자일 때
        if target == s[i]:
            cnt1 += 1
        # 다른 글자 일때
        else:
            cnt2 += 1
        # 지금까지 나온 갯수가 같을 경우
        if cnt1 == cnt2:
            answer += 1
            cnt1, cnt2 = 0, 0
            target = ""
    # cnt가 초기화 되지 않았다면 뒤에 나머지 부분이 존재한다
    if cnt1 != cnt2:
        answer += 1
    return answer