t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    member_list = list(map(int, input().split()))
    result_list = []
    for i in range(n):
        if i + 1 not in member_list:
            result_list.append(i + 1)
    print(f"#{tc + 1}", *result_list)