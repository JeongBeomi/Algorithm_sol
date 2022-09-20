t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    b_num =  format(m, 'b')
    result = "ON"
    for i in range(1, n + 1):
        if len(b_num) < n or b_num[-i] == '0':
            result = "OFF"
            break
    print(f"#{tc + 1} {result}")