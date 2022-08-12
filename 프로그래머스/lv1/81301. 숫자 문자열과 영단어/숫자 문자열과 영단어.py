def solution(s):
    en_numbers_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for idx, en_num in enumerate(en_numbers_list):
        s = s.replace(en_num, str(idx))
    return int(s)