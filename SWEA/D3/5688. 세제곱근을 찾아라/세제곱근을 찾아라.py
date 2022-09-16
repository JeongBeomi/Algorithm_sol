t = int(input())
for tc in range(t):
    n1 = int(input())
    n2 = n1 ** (1/3)
    print(f"#{tc + 1}", end=" ")
    if round(n2) ** 3 == n1:
        print(round(n2))
    else:
        print(-1)