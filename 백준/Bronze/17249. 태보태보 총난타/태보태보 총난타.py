string = input()
total_cnt = string.count("@")
left_cnt = string[0:string.find("(")].count("@")
print(left_cnt, total_cnt - left_cnt)