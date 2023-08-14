word_list = ["A", "E", "I", "O", "U"]

# 인데스로 이루어진 리스틑 문자열로 바꿔줌
def idx_to_string(arr):
    result = ""
    for i in arr:
        result += word_list[i]
    return result
        
def solution(word):
    answer = 0
    temp = []
    # 같을 때까지 탐색
    while idx_to_string(temp) != word:
        # 다음 숫자로 넘어가기
        answer += 1
        # 모음 조합이 다섯개가 안될때 A 추가
        if len(temp) < 5:
            temp.append(0)
        # 모음 조합 다섯개 일때
        else:
            temp[-1] += 1
            # 마지막 모음이 U를 넘어가면 앞의 인덱스 바꾸기
            while temp[-1] >= 5:
                temp.pop()
                temp[-1] += 1
            
    return answer