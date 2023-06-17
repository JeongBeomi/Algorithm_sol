n = int(input())
oil = list(map(int, input().split()))
oil_price = list(map(int, input().split()))
result = 0

min_price = oil_price[0]
for i in range(n - 1):
    if min_price > oil_price[i]:
        min_price = oil_price[i]

    result += min_price * oil[i]

print(result)