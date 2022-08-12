string = input()

cro_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
cnt = 0
for char in cro_list:
    if string.count(char):
        cnt += string.count(char)
        string = string.replace(char, " ")
string = string.replace(" ", "")
print(cnt + len(string))