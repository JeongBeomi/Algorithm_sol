t = int(input())
for _ in range(t):
    ox_list = input()
    add_score = 1
    answer = 0
    for i in ox_list:
        if i == "O":
            answer += add_score
            add_score += 1
        else:
            add_score = 1
    print(answer)