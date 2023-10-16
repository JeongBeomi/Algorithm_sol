def solution(n, words):
    answer = [0, 0]
    # 중복체크를 위한 단어집합 생성
    word_set = set()
    word_set.add(words[0])
    # 두번째 단어부터 확인
    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0] or words[i] in word_set:
            answer = [i % n + 1, i // n + 1]
            break
        word_set.add(words[i])
        
    return answer