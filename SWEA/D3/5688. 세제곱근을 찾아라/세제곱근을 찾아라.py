t = int(input())
for tc in range(t):
    n = int(input())
    result = -1
    i = 0
    while True:
        i += 1
        if i ** 3 == n:
            result = i
            break
        elif i ** 3 > n:
            break
    print(f"#{tc + 1} {result}")