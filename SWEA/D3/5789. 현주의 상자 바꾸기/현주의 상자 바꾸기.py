
t = int(input())
for tc in range(t):
    n, q = map(int, input().split())

    box_list = [0] * n
    for i in range(q):
        l, r = map(int, input().split())
        for j in range(l-1, r):
            box_list[j] = i+1

    print(f"#{tc+1}", end=" ")
    print(*box_list)