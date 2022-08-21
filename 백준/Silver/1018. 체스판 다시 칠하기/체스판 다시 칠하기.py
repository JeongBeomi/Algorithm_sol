n, m = map(int, input().split())
input_map = [list(input()) for _ in range(n)]
min_cnt = n * m

for k in range(2):
    for row in range(n - 8 + 1):
        for col in range(m - 8 + 1):
            flag = 0
            cnt = 0
            flag += k
            for i in range(8):
                for j in range(8):
                    if flag % 2:
                        if input_map[row + i][col + j] != "W":
                            cnt += 1
                    else:
                        if input_map[row + i][col + j] != "B":
                            cnt += 1
                    flag += 1
                flag += 1
            if min_cnt > cnt:
                min_cnt = cnt
print(min_cnt)