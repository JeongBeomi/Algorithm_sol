t = int(input())
for tc in range(t):
    string_list = [input() for _ in range(5)]
    print(f"#{tc+1}", end=" ")
    for i in range(15):
        for string_line in string_list:
            if i >= len(string_line):
                continue
            print(string_line[i], end="")
    print()