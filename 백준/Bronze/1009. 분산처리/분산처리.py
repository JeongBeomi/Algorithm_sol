t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    if b%4 == 0:
        total = a** 4
    else:
        total = a ** (b % 4)
    if total % 10 ==0:
        print(10)
    else:
        print(total % 10)
