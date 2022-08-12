t = int(input())

for tc in range(t):
    n = int(input())
    str_numbers = input()
    str_numbers = str_numbers.replace("0", " ")

    max_cnt = 0
    for i in str_numbers.split():
        if max_cnt < len(i):
            max_cnt = len(i)

    print(f"#{tc+1} {max_cnt}")