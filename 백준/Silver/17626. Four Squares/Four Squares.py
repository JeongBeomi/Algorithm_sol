n = int(input())
memo = [5000] * (n + 1)
memo[0], memo[1] = 0, 1

for i in range(2, n + 1):
    for j in range(1, int(i ** 0.5) + 1):
        memo[i] = min(memo[i], 1 + memo[i - (j ** 2)])

print(memo[n])