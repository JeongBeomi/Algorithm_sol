t = int(input())
for tc in range(t):
    memo = list(map(int, input()))

    flag = False
    cnt = 0
    for i in memo:
        if not flag and i == 1:
            cnt += 1
            flag = True
        elif flag and i == 0:
            cnt += 1
            flag = False
    print(f"#{tc + 1} {cnt}")