def solution(s):
    n = len(s)
    answer = n
    # 압축하는 단위가 문자열 길이의 절반이 넘어가면 더이상 압축 불가능
    for i in range(1, n + 1 // 2):
        idx = 0
        zip_string = ""
        cnt = 0
        repeat_string = s[0 : i]
        # 반복문자 확인
        while idx < n:
            if s[idx : idx + i] == repeat_string:
                cnt += 1
                idx += i
            else:
                if cnt == 1:
                    zip_string += repeat_string
                else:
                    zip_string += str(cnt) + repeat_string
                repeat_string = s[idx : idx + i]
                cnt = 0
        # 마지막 문자열 붙여주기
        if cnt == 1:
            zip_string += repeat_string
        else:
            zip_string += str(cnt) + repeat_string
        repeat_string = s[idx : idx + i]

        if len(zip_string) < answer:
            answer = len(zip_string)
            
    return answer
