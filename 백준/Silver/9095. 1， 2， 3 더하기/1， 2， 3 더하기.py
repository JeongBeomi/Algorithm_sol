memo = [1, 2, 4]

t = int(input())

for _ in range(t):
    n = int(input())
    if len(memo) < n:
        for i in range(len(memo), n):
            memo.append(memo[i - 1] + memo[i - 2] + memo[i - 3])
    print(memo[n - 1])