def secret(q):
    while True:
        for i in range(1,6):
            num = q.pop(0)
            if num - (i) <= 0:
                q.append(0)
                return
            q.append(num - i)

for _ in range(10):
    n = int(input())
    q = list(map(int, input().split()))
    secret(q)
    print(f"#{n}", *q)