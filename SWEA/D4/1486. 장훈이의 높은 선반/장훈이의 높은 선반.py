t = int(input())
for tc in range(t):
    n, b = map(int, input().split())
    height_list = list(map(int, input().split()))
    result_list = []
    for i in range(1 << n):
        total_height = 0
        for j in range(n):
            if i & (1 << j):
                total_height += height_list[j]
        if total_height >= b:
            result_list.append(total_height - b)
    print(f"#{tc + 1} {min(result_list)}")