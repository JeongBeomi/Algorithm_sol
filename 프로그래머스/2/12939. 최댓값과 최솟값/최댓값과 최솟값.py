def solution(s):
    sorted_nums = sorted(map(int, s.split()))
    return "{} {}".format(sorted_nums[0], sorted_nums[-1])
    