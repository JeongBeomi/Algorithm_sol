def solution(s):
    num_list = sorted(list(map(int, list(s.split()))))
    return " ".join([str(num_list[0]), str(num_list[-1])])
