def solution(s, n):
    answer = ''
    upper_alpa = list(range(65, 91))
    lower_alpa = list(range(97, 123))
    #97~122, 65~90
    for ch in s:
        if 97 <= ord(ch) <= 122:
            answer += chr(lower_alpa[(lower_alpa.index(ord(ch)) + n) % len(lower_alpa)])
        elif 64 <= ord(ch) <= 90:
            answer += chr(upper_alpa[(upper_alpa.index(ord(ch)) + n) % len(upper_alpa)])
        else:
            answer += ch
    return answer