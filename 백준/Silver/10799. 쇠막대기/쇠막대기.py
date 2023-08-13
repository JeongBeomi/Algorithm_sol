bars_list = list(input())
answer = 0
# 스택
s = []
# 괄호 정보 순서대로 확인
for bar_idx in range(len(bars_list)):
    # ) 가 나오면 레이저 or 하나의 막대기가 끝남
    if bars_list[bar_idx] == ")":
        s.pop()
        # 직전이 ( 이면 레이저
        if bars_list[bar_idx - 1] == "(":
            answer += len(s)
        # 직전 괄호가 ) 이면 막대가 하나 끝난것
        else:
            answer += 1
    # ( 일때는 스텍에 추가
    else:
        s.append(bars_list[bar_idx])

print(answer)