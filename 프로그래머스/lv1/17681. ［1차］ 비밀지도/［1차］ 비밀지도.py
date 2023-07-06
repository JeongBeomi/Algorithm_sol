def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # 두개의 지도에서 벽에 해당하는 부분을 찾기 위해 or비트연산자 | 사용 
        secret_map = arr1[i] | arr2[i]
        # 쉬프트 연산을 통해 한줄의 각 칸이 벽인지 확인
        line = ""
        for j in range(n):
            if secret_map & (1 << j):
                line = "#" + line
            else:
                line = " " + line
        answer.append(line)
        # 쉬프트연산을 반복하기보다는 정수를 2진수 문자열로 바꾼 후 반복문사용이 더 좋은가?
        
    return answer