list_a = [list(input()) for _ in range(8)]

flag = 0
cnt = 0
for i in range(8):
    for j in range(8):
        if flag % 2 == 0 and list_a[i][j] == "F":
            cnt += 1
        flag += 1
    flag += 1
print(cnt)