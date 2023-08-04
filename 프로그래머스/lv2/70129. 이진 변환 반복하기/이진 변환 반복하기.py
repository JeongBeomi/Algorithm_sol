def solution(s):
    # 이진변환횟수, 제거한 0 수
    answer = [0, 0]
    while s != "1":
        # 문자열에서 0제거
        del_zero = "".join(s.split("0"))
        # 이진변환수, 제거한 0 수 업데이트
        cnt = len(del_zero)
        answer[1] += len(s) - cnt 
        answer[0] += 1
        # 이진 변환 결과를 s에 저장
        s = str(bin(cnt))[2:]
        
    return answer