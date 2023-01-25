total = int(input())
n = int(input())
for _ in range(n):
    m, x = map(int, input().split())
    total -= m * x
if total == 0:
    print("Yes")
else:
    print("No")