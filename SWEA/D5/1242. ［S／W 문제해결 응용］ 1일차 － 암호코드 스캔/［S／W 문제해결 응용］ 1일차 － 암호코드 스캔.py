secret_code = {
    (2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4,
    (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9,
}

t = int(input())
for tc in range(t):
    result = 0
    n, m = map(int, input().split())
    input_lines = list(set([input().strip().lstrip('0') for _ in range(n)])) # 중복 제거
    password = []
    for x_nums in input_lines:   # 한줄만 먼저 들고와서
        if x_nums == "":
            continue
        bin_line = ""
        bin_line += format(int(x_nums, 16), 'b')     # 16진수 -> 2진수)
        n1, n2, n3 = 0, 0, 0    # 암호코드 적용을 위한 비율 
        secret_nums = []

        for num in bin_line:    # 한줄에서 나오는 암호코드 찾기
            if num == '1' and n2 == 0:
                n1 += 1
            elif num == '0' and n1 != 0 and n3 == 0:
                n2 += 1
            elif num == '1' and n2 != 0:
                n3 += 1
            elif n3 != 0:       # 암호코드 1개의 비율찾기가 끝나면
                min_n = min(n1, n2, n3)     # 가장 작은 값으로 나눠주면 최소비율
                secret_nums.append(secret_code[(n1 // min_n, n2 // min_n, n3 // min_n)])
                n1, n2, n3 = 0, 0, 0        # 다음 암호번호 1개를 찾기위해 비율 초기화

        for i in range(0, len(secret_nums), 8): # 한줄 탐색이 끝나면 8개씩 나눠서 검증 코드 확인
            if secret_nums[i : i + 8] in password:
                continue
            odd = sum((secret_nums[i], secret_nums[i + 2], secret_nums[i + 4], secret_nums[i + 6]))
            even = sum((secret_nums[i + 1], secret_nums[i + 3], secret_nums[i + 5]))
            src_num = secret_nums[i + 7]
            if (odd * 3 + even + src_num) % 10 == 0:
                password.append(secret_nums[i : i + 8])
                result += odd + even + src_num

    print(f"#{tc + 1} {result}")