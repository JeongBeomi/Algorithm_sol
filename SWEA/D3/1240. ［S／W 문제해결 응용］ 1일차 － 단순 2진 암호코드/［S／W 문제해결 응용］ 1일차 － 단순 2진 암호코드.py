codes = {
    (2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3, (1, 3, 2): 4,
    (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7, (2, 1, 3): 8, (1, 1, 2): 9,
}


t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    lines = list(set([(input().strip()).lstrip('0') for _ in range(n)]))    # n3카운트 끝나는 점을 알기 위해 뒤에 0은 남긴다.
    numbers = []    # 해석한 암호를 담기 위한 리스트
    answer = 0
    for line in lines:  # 한줄먼저 들고온다.
        n1, n2, n3 = 0, 0, 0
        for i in line:  # 암호 해석 시작
            if i == '1' and not n2:
                n1 += 1
            elif i == '0' and n1 and not n3:
                n2 += 1
            elif i == '1' and n2:
                n3 += 1
            elif n3:
                min_v = min(n1, n2, n3)
                numbers.append(codes[(n1//min_v, n2//min_v, n3//min_v)])
                n1, n2, n3 = 0, 0, 0
    odd = sum(numbers[::2])
    even = sum(numbers[1:-1:2])
    if (odd * 3 + even + numbers[-1]) % 10 == 0:
        answer += sum(numbers)
    print(f"#{tc + 1} {answer}")