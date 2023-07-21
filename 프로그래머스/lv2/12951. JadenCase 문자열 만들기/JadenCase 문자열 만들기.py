def solution(s):
    answer = ''
    word_list = list(s)
    first_ch = 1
    for i in range(len(word_list)):
        if word_list[i] == " ":
            answer += word_list[i]
            first_ch = 1
        else:
            if first_ch:
                answer += word_list[i].upper()
                first_ch = 0
            else:
                answer += word_list[i].lower()
    # for i in range(len(word_list)):
    #     word_list[i] = word_list[i].capitalize()
    # answer = " ".join(word_list)
    return answer