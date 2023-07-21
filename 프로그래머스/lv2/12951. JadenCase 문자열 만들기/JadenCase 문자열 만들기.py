def solution(s):
    answer = ''
    word_list = s.split(" ")
    for i in range(len(word_list)):
        word_list[i] = word_list[i].capitalize()
    answer = " ".join(word_list)
    return answer