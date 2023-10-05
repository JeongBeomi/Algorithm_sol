n = int(input())
boxes = list(map(int, input().split()))
memo = [1] * n
for i in range(1, n):
    for j in range(i):
        if boxes[j] < boxes[i]:
            memo[i] = max(memo[i], memo[j] + 1)

print(max(memo))