# def solution(s, n):
#     answer = ''
#     upper_alpa = list(range(65, 91))
#     lower_alpa = list(range(97, 123))
    
#     for ch in s:
#         # 소문자
#         if 97 <= ord(ch) <= 122:
#             answer += chr(lower_alpa[(lower_alpa.index(ord(ch)) + n) % len(lower_alpa)])
#         # 대문자
#         elif 65 <= ord(ch) <= 90:
#             answer += chr(upper_alpa[(upper_alpa.index(ord(ch)) + n) % len(upper_alpa)])
#         # 공백
#         else:
#             answer += ch
#     return answer

def solution(s, n):
    answer = ''
    
    for alpha in s:
        alpha_i = ord(alpha)
        # if alpha_i >= 65 and alpha_i < 91:      # 대문자
        if 65 <= alpha_i < 91:      # 대문자
            # answer += chr(((alpha_i+n)//91)*64 + (alpha_i+n)%90)
            answer += chr(((alpha_i+n)//91)*65 + (alpha_i+n)%91)
        # elif alpha_i >= 97 and alpha_i < 123:   # 소문자
        elif 97<= alpha_i < 123:   # 소문자
            answer += chr(((alpha_i+n)//123)*97 + (alpha_i+n)%123)
        else:                                   # 공백
            answer += " "
    # print(ord('a')+25)
    return answer