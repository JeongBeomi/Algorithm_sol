def per(start, end, length, num):
    if len(num) == length:
        print(*num)
        return
    for i in range(start, end):
        num.append(num_list[i])
        per(i + 1, end, length, num)
        num.pop()

n, m = map(int, input().split())
num_list = list(range(1, n + 1))
per(0, n, m, [])