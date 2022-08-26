t = int(input())
for tc in range(t):
    n = int(input())
    numbers_list = list(map(int, input().split()))
    danjo = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            num = numbers_list[i] * numbers_list[j]
            if num <= 10:
                break
            num_list = []

            while num:
                num_list.append(num % 10)
                num = num // 10

            for k in range(len(num_list) - 1):
                if num_list[k] < num_list[k + 1]:
                    break
            else:
                danjo.append(numbers_list[i] * numbers_list[j])
            # num_list = list(map(int, str(num)))
            # for k in range(len(num_list) - 1):
            #     if num_list[k] > num_list[k + 1]:
            #         break
            # else:
            #     danjo.append(num)

    if not danjo:
        print(f"#{tc + 1} -1")
    else:
        print(f"#{tc + 1} {max(danjo)}")