string = input()

cro_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for char in cro_list:
    string = string.replace(char, " ")
print(len(string))