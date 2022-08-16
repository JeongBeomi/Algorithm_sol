def palindrome_detect(arr, m):
    for string_line in arr:
        for j in range(100-m+1):
            if string_line[j: j+m] == string_line[j:j+m][::-1]:
                return True
    return False

for _ in range(10):
    tc = int(input())
    string_list = [input() for _ in range(100)]
    max_cnt = 1

    # 가장 긴 회문을 찾기 때문에 길이 100인 회문 부터 찾기 시작
    for i in range(100, 0, -1):
        if palindrome_detect(string_list, i) or palindrome_detect(zip(*string_list), i):
            print(f"#{tc} {i}")
            break